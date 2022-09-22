# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

from collections import defaultdict


def solution(N, stages):
    count = len(stages)
    result = []

    stage_dict = defaultdict(int)

    for stage in stages:
        stage_dict[stage] += 1  # 도달하지 못한 사용자

    result_list = []

    for i in range(1, N + 1):
        if count != 0:
            result_list.append([-stage_dict[i] / count, i])
        else:
            result_list.append([1, i])
        count -= stage_dict[i]
    result_list = sorted(result_list)
    while result_list:
        result.append(result_list.pop(0)[1])

    return result

"""
N = 5 / stages = [2, 1, 2, 6, 2, 4, 3, 3] / return = [3, 4, 2, 1, 5]
N = 4 / stages = [4, 4, 4, 4, 4] / return = [4, 1, 2, 3]
"""