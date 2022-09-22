#  각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
# 단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다.
# 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.
# 각 손님들이 주문한 단품메뉴들이 문자열 형식으로 -> orders ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# 코스 요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course [2,3,4]
from itertools import combinations


def solution(orders, course):
    answer = []
    for i in course:
        test = make_combination_dic(i, sorted(orders))
        if test:
            max_value = max(test.values())
            if max_value == 1:
                continue
            for every_key in test.keys():
                if test[every_key] == max_value:
                    answer.append("".join(every_key))
        else:
            continue

    answer = sorted(answer)

    return answer


def make_combination_dic(r, orders):
    result = {}
    for every_order in orders:
        trans = list(every_order)
        for every_combination in combinations(trans, r):
            if "".join(sorted(list(every_combination))) not in result.keys():
                result["".join(sorted(list(every_combination)))] = 1
            else:
                result["".join(sorted(list(every_combination)))] = result["".join(sorted(list(every_combination)))] + 1
    return result

"""
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
return = ["AC", "ACDE", "BCFG", "CDE"]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
return = ["ACD", "AD", "ADE", "CD", "XYZ"]

orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
return = ["WX", "XY"]
"""