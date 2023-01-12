from collections import defaultdict
def solution(s, times):
    answer = []
    c_1 = lambda x: int(x[0:4]) * 12 * 30 * 3600 * 24 + int(x[5:7]) * 30 * 3600 * 24 + int(x[8:10]) * 3600 * 24 + int(
        x[11:13]) * 3600 + int(x[14:16]) * 60 + int(x[17:19])
    c_2 = lambda x : int(x[0:2]) * 3600 * 24 + int(x[3:5]) * 3600 + int(x[6:8])*60 + int(x[9:11])
    convert_day = 24*3600
    cur_time = c_1(s)
    day_list = [cur_time // convert_day]
    for time in times:
        add_time = c_2(time)
        cur_time += add_time
        day_list.append(cur_time // convert_day)

    day_list = set(day_list)
    count = 0
    min_day = min(day_list)
    max_day = max(day_list)
    for d in range(min_day, max_day + 1):
        if d not in day_list:
            answer.append(0)
            break
    if not answer:
        answer.append(1)

    answer.append(max_day - min_day + 1)
    print(answer)
    return answer
solution("1997:03:14:00:00:00", ["00:00:00:00"])