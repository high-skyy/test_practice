# 인적사항 정리
# 후보 키 (유일하게 분류하며 최소인 것)
# 후보 키의 최대 개수
# relation [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"] ...

from collections import defaultdict
from itertools import combinations


def solution(relation):
    answer = 0

    index_list = [i for i in range(len(relation[0]))]
    length = len(index_list)

    key_dict = defaultdict(int)
    candidate = []

    for i in range(1, length + 1):
        for comb in combinations(index_list, i):
            trigger = False
            for r in relation:
                key = []
                for index in comb:
                    key.append(r[index])
                    key.append(index)
                if key_dict[tuple(key)]:
                    trigger = True
                    break
                else:
                    key_dict[tuple(key)] = 1
            if not check_in(comb, candidate) and not trigger:
                candidate.append(list(comb))
    answer = len(candidate)
    return answer


def check_in(check, candidate):
    check_set = set(check)
    if len(candidate) == 0:
        return False
    for every in candidate:
        every_set = set(every)
        if every_set == set.intersection(check_set, every_set):
            return True
    return False

"""
relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
return = 2
"""