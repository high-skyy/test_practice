# 왼쪽 숫자 : 직원번호 (1번부터 순서대로 발급됨) 오른쪽 숫자 : 해당 직원의 하루평균 매출액
# 팀장과 팀원 (CEO->항상 팀장 / 나머지는 항상 화살표 하나 받음)
# 2개의 팀에 속할 수 있으며 하나의 팀에서는 팀장 하나의 팀에서는 팀원이여야 한다.
# 모든 팀은 최소 1명 이상의 직원을 워크숍에 참석
# 워크숍에 참석하는 직원들의 하루평균 매출액의 합이 최소
# sales(2이상 300,000 이하) 각 원소는 0이상 10,000이하 하루평균 매출액 값 [14, 17, 15, 18, 19, 14, 13, 16, 28, 17] (index + 1이 직원번호)
# links sales 배열의 크기 - 1 (팀장-팀원) [a, b] a : 직원 번호, b : a팀장이 관리하는 팀원의 직원번호 [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]

from collections import defaultdict
from collections import deque


def solution(sales, links):
    answer = 0

    tree = defaultdict(list)
    v_tree = defaultdict(dict)

    for link in links:
        tree[link[0]].append(link[1])
    print(tree)
    dq = deque()
    dq.append(1)
    visited = [1]
    while dq:
        cur_node = dq.popleft()
        for next_node in tree[cur_node]:
            visited.append(next_node)
            dq.append(next_node)

    while visited:
        cur_node = visited.pop()
        # leafnode의 경우
        if not tree[cur_node]:
            v_tree[cur_node]["Y"] = sales[cur_node - 1]
            v_tree[cur_node]["N"] = 0
        else:
            child = tree[cur_node]
            perm = []
            permutation(child, [], perm)
            values = []
            for ny_list in perm:
                value = 0
                for num, ny in zip(child, ny_list):
                    value += v_tree[num][ny]
                values.append(value)
            v_tree[cur_node]["Y"] = min(values) + sales[cur_node - 1]
            v_tree[cur_node]["N"] = min(values[1:])
    answer = min([v_tree[1][i] for i in ["Y", "N"]])
    return answer


def permutation(child, temp, result):
    if len(child) != len(temp):
        temp_1, temp_2 = temp[:], temp[:]
        temp_1.append("N")
        temp_2.append("Y")
        permutation(child, temp_1, result)
        permutation(child, temp_2, result)
    else:
        result.append(temp)
        return

"""
sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17] / links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
return = 44

sales = [5, 6, 5, 3, 4] / links = [[2, 3], [1, 4], [2, 5], [1, 2]]
return = 6

sales = [5, 6, 5, 1, 4] / links = [[2, 3], [1, 4], [2, 5], [1, 2]]
return = 5

sales = [10, 10, 1, 1] / links = [[3, 2], [4, 3], [1, 4]]
return = 2
"""
