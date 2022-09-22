# 시청자들이 가장 많이 보는 구간에 공익광고를 넣으려고 합니다.
#  "죠르디"는 시청자들이 해당 동영상의 어떤 구간을 재생했는 지 알 수 있는 재생구간 기록을 구했고, 해당 기록을 바탕으로 공익광고가 삽입될 최적의 위치를 고를 수 있었습니다.
# 누적 재생시간 이 가장 긴 곳 선택 (각자 구하는 방법은 그냥 뒤에서 앞 빼면됨)
# 동영상 재생시간 길이 play_time, 공익광고의 재생시간 길이 adv_time, 구간 정보 logs (answer = 시작시각 8자리 문자배열로 반환) (여러곳 가장 빠른 시각)
# play_time, adv_time은 HH:MM:SS 형식이며, 00:00:01 이상 99:59:59 이하
# logs(크기 1이상 300,000 이하 문자 배열) 배열의 각 원소는 H1:M1:S1-H2:M2:S2

from collections import deque


def solution(play_time, adv_time, logs):
    max_value = 0
    answer = ""
    start_point = []
    # str -> int
    play_dur = int(play_time[0:2]) * 3600 + int(play_time[3:5]) * 60 + int(play_time[6:8])
    adv_dur = int(adv_time[0:2]) * 3600 + int(adv_time[3:5]) * 60 + int(adv_time[6:8])

    # print(play_dur, adv_dur)
    acc = [0 for _ in range(play_dur + 1)]

    for element in logs:
        start = int(element[0:2]) * 3600 + int(element[3:5]) * 60 + int(element[6:8])
        end = int(element[9:11]) * 3600 + int(element[12:14]) * 60 + int(element[15:17])
        acc[start] += 1
        acc[end] -= 1

    for i in range(play_dur):
        acc[i + 1] = acc[i] + acc[i + 1]

    start, end, value = 0, adv_dur, 0
    value = sum(acc[start:end])
    print(value)
    max_value = value
    start_point.append(0)

    while end < play_dur:
        value += (acc[end] - acc[start])
        end += 1
        start += 1
        if value > max_value:
            start_point.clear()
            start_point.append(start)
            max_value = value
    # print(start_point)
    answer_int = min(start_point)
    hour = int(answer_int / 3600)
    minutes = int((answer_int - 3600 * hour) / 60)
    second = answer_int - 3600 * hour - 60 * minutes
    answer = f"{hour:2}:{minutes:2}:{second:2}"
    print(type(answer))

    return answer

"""
play_time = "02:03:55" / adv_time = "00:14:15" / logs = ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]
return = "01:30:59"

play_time = "99:59:59" / adv_time = "25:00:00" / logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
return = "01:00:00"

play_time = "50:00:00" / adv_time = "50:00:00" / logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
return = "00:00:00"
"""