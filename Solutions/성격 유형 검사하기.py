# 각 질문은 1가지 지표로 성격 유형 점수를 판단한다.
# 동점 -> 사전순 처리
# (R, T) (C, F), (J, M), (A, N)

from collections import defaultdict


def solution(survey, choices):
    answer = ''
    check_list = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    result_in_sum = defaultdict(int)

    for i in range(len(survey)):
        left, right = survey[i]
        point = choices[i]
        if point < 4:
            result_in_sum[left] += abs(point - 4)
        else:
            result_in_sum[right] += abs(point - 4)
    print(result_in_sum)
    for criteria in check_list:
        if result_in_sum[criteria[0]] > result_in_sum[criteria[1]]:
            answer += criteria[0]
        elif result_in_sum[criteria[0]] < result_in_sum[criteria[1]]:
            answer += criteria[1]
        else:
            if criteria[0] < criteria[1]:
                answer += criteria[0]
            else:
                answer += criteria[1]
    return answer