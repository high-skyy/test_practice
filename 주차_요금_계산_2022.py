"""
어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주합니다
00:00부터 23:59까지의 입/출차 내역을 바탕으로 차량별 누적 주차 시간을 계산하여 요금을 일괄로 정산합니다.
누적 주차 시간이 기본 시간이하-> 기본 요금을 청구합니다.
누적 주차 시간이 기본 시간을 초과-> 기본 요금에 더해서, 초과한 시간에 대해서 단위 시간 마다 단위 요금을 청구합니다.
초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림합니다.
⌈a⌉ : a보다 작지 않은 최소의 정수를 의미합니다. 즉, 올림을 의미합니다.
주차 요금을 나타내는 정수 배열 fees, 자동차의 입/출차 내역을 나타내는 문자열 배열 records가 매개변수로 주어집니다.
번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
"""


def calculate_minutes(data_list):
    # [[960, 3961, 0], [1080, 3961, 1], [1438, 3961, 0]]
    # print("data_list : ", data_list)
    in_minute = []
    out_minute = []
    for every_data in data_list:
        # print("every_data is : ", every_data)
        # print("every_data[2] is : ",every_data[2])
        if every_data[2] == 0:
            # print("in_minute append")
            in_minute.append(every_data[0])
            # print("in_minute (중간) : ", in_minute)
        elif every_data[2] == 1:
            # print("out_minute append")
            out_minute.append(every_data[0])
            # print("out_minute (중간) : ", out_minute)
        else:
            print("error in in/out")
    tot_minute = 0
    # print("in_minute : ", in_minute)
    # print("out_minute : ", out_minute)
    if len(in_minute) != len(out_minute):
        for i in out_minute:
            tot_minute = tot_minute + i
        tot_minute = tot_minute + 60 * 23 + 59
        for j in in_minute:
            tot_minute = tot_minute - j
        return tot_minute
    else:
        for i in out_minute:
            tot_minute = tot_minute + i
        for j in in_minute:
            tot_minute = tot_minute - j
        return tot_minute


def calculate_fee(minute, fees):
    if minute <= fees[0]:
        return fees[1]
    else:
        num_minute = minute - fees[0]
        if num_minute % fees[2] != 0:
            return fees[1] + (int(num_minute / fees[2]) + 1) * fees[3]
        else:
            return fees[1] + int(num_minute / fees[2]) * fees[3]


def solution(fees, records):
    # fees // 길이 : 4 [기본시간, 기본요금, 단위 시간, 단위 요금]
    # records // ["시각 차량번호 내역", ... ] 공백 구분
    # 시각 : 입차 or 출차 HH:MM 형식의 길이 5인 문자열 (제대로 된 시간만 입력 됨)
    # 차량번호 : 0 ~ 9 로 구성된 길이 4인 문자열
    # 내역 : 길이 2 또는 3인 문자열로 IN 또는 OUT 입니다.
    # records의 원소들은 시각을 기준으로 오름차순으로 정렬
    # 다음 날 출차 입력으로 주어지지 x
    # 마지막 시각(23:59) 에 입차 -> 입력으로 주어지지 않는다.
    answer = []
    # records // ["시각 차량번호 내역", ... ] -> 형식 ["시각(숫자), 차량번호 숫자, 내역(숫자)"] 바꾸기
    converted_records = []
    car_number_list = []
    for every_records in records:
        time, number, in_out = map(str, every_records.split(' '))
        temp_list = []
        hour, minute = map(int, time.split(':'))
        tot_time = hour * 60 + minute
        # print("total time is : ", tot_time)
        temp_list.append(tot_time)
        temp_list.append(int(number))
        car_number_list.append(int(number))
        # print("car_number is : ", number)
        if in_out == 'IN':
            temp_list.append(0)
        elif in_out == 'OUT':
            temp_list.append(1)
        else:
            print("Error in IN/OUT")
        # print("in_out is : ", in_out)
        converted_records.append(temp_list)
    print("converted_records : ", converted_records)
    car_number_list = set(car_number_list)
    # print("car_number_set :", car_number_list)
    minute_data_list = []
    while len(car_number_list) != 0:
        min_car_number = min(car_number_list)
        # print("min_car_number is : ", min_car_number)
        car_number_list.remove(min_car_number)
        data_list = []
        # print(type(min_car_number))
        # print(type(converted_records[0][1]))
        for every_car_data in converted_records:
            if every_car_data[1] == min_car_number:
                data_list.append(every_car_data)
        minute_data_list.append(calculate_minutes(data_list))
    print("minute_data_list : ", minute_data_list)
    for every_minute_data in minute_data_list:
        answer.append(calculate_fee(every_minute_data, fees))
    print("answer is : ", answer)
    return answer

"""
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
return = [14600, 34400, 5000]
"""

