# 특정 범위 물건 다 삼
# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간 (일직선)]
# [시작번호, 끝 번호] return 짧은 구간이 여러개 -> 사각 진열대 번호 작은 것

from collections import defaultdict


def solution(gems):
    answer = []

    # two-pointer
    # length로 구현
    gem_type_num = len(set(gems))
    gem_num_dict = defaultdict(int)

    # initialize (마지막 1 추가해 줘야함)
    start_index = 0
    end_index = 0
    min_value = 100002
    min_result = [1, 100002]

    if gem_type_num == 1:
        return [1, 1]

    gem_num_dict[gems[0]] += 1
    while True:
        # 검사

        if len(gem_num_dict) == gem_type_num:
            length = end_index - start_index
            if min_value > length:
                min_value = length
                min_result = [start_index + 1, end_index + 1]

        if len(gem_num_dict) == gem_type_num:
            if start_index + 1 <= len(gems) - 1:
                gem_num_dict[gems[start_index]] -= 1
                if gem_num_dict[gems[start_index]] == 0:
                    del gem_num_dict[gems[start_index]]
                start_index += 1
        else:
            if end_index + 1 <= len(gems) - 1:
                end_index += 1
                gem_num_dict[gems[end_index]] += 1
            else:
                break

    answer = min_result

    return answer