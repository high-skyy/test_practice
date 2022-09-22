"""
초당 최대 처리량은 요청의 응답 완료 여부에 관계없이 임의 시간부터 1초(=1,000밀리초)간 처리하는 요청의 최대 개수를 의미한다.
"""


# solution 함수에 전달되는 lines 배열은 N(1 ≦ N ≦ 2,000)개의 로그 문자열로 되어 있으며, 각 로그 문자열마다 요청에 대한 응답완료시간 S와 처리시간 T가 공백으로 구분되어 있다.
# 응답완료시간 S는 작년 추석인 2016년 9월 15일만 포함하여 고정 길이 2016-09-15 hh:mm:ss.sss 형식으로 되어 있다.
# 처리시간 T는 0.1s, 0.312s, 2s 와 같이 최대 소수점 셋째 자리까지 기록하며 뒤에는 초 단위를 의미하는 s로 끝난다.
# (처리시간은 시작시간과 끝시간을 포함)
# lines 배열은 응답완료시간 S를 기준으로 오름차순 정렬되어 있다.

def solution(lines):
    # 데이터 정리
    clean_data = []
    for every_line in lines:
        data, T, S = every_line.split(' ')
        hour, minute, second = map(float, T.split(":"))
        end_time = round(hour * 3600 + 60 * minute + second, 3)
        S = float(S.split('s')[0])
        start_time = round(end_time - S + 0.001, 3)
        trans_data = [start_time, end_time]
        clean_data.append(trans_data)
    print(clean_data)
    # 갯수 찾기
    global max_num
    max_num = 0
    for i in range(len(clean_data)):
        num = 1
        end_time = clean_data[i][1]
        threshold = round(end_time + 1 - 0.001, 3)
        # print(threshold)
        for j in range(i + 1, len(clean_data)):
            if clean_data[j][0] <= threshold:
                num = num + 1
        if max_num < num:
            max_num = num

    answer = max_num
    return answer

"""
lines = ["2016-09-15 00:00:00.000 3s"]
return 1
lines = ["2016-09-15 23:59:59.999 0.001s"]
return 1
lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
return 1
lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
return 2
lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
return 7
lines = ["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]
return 1
"""