#  지점의 개수 n, 출발지점을 나타내는 s, A의 도착지점을 나타내는 a, B의 도착지점을 나타내는 b, 지점 사이의 예상 택시요금을 나타내는 fares가 매개변수로 주어집니다
# 지점갯수 n은 3 이상 200 이하인 자연수입니다.
#  s, a, b는 1 이상 n 이하인 자연수이며, 각기 서로 다른 값입니다
# c지점과 d지점 사이의 예상 택시요금이 f원이라는 뜻입니다. fares[index] = [c,d,f]
# fares 배열에 두 지점 간 예상 택시요금은 1개만 주어집니다. 즉, [c, d, f]가 있다면 [d, c, f]는 주어지지 않습니다.

from collections import defaultdict
import heapq


# 최소 거리 구하고 그 노드에서 부터 A 지점 B 지점 까지의 거리 구하고
# 지점 까지 같이 간 거리(최소 거리) + A 지점까지 + B지점 까지의 거리
# 해당 노드로의 최소 거리가 구한 값 보다 크면 그대로 return 시킨다

# 워샬 알고리즘 (해봄)
# 디엑스트라 알고리즘 (아직)

def solution(n, s, a, b, fares):
    answer = 0

    max_val = 100000 * n * (n - 1)
    min_val = max_val
    nodes = defaultdict(dict)
    new_fares = defaultdict(list)

    for node_1, node_2, fare in fares:
        new_fares[node_1].append([fare, node_2])
        new_fares[node_2].append([fare, node_1])

    for i in range(n):
        nodes[i + 1] = {"min_dist": max_val, "a_dist": max_val, "b_dist": max_val}
    dyx(new_fares, "min_dist", s, nodes, n)
    dyx(new_fares, "a_dist", a, nodes, n)
    dyx(new_fares, "b_dist", b, nodes, n)
    for key in nodes.keys():
        if min_val > nodes[key]["min_dist"] + nodes[key]["a_dist"] + nodes[key]["b_dist"]:
            min_val = nodes[key]["min_dist"] + nodes[key]["a_dist"] + nodes[key]["b_dist"]
    answer = min_val
    return answer


def dyx(new_fares, index, start_node, nodes, n):
    visited = []
    nodes[start_node][index] = 0
    paths = [[0, start_node]]
    while paths:
        fare, cur_node = heapq.heappop(paths)
        if cur_node in visited:
            continue
        else:
            visited.append(cur_node)
            for next_fare, next_node in new_fares[cur_node]:
                nodes[next_node][index] = min(nodes[next_node][index], nodes[cur_node][index] + next_fare)
                heapq.heappush(paths, [nodes[next_node][index], next_node])



"""
n = 6 / s = 4 / a = 6 / b = 2 / fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
return = 82

n = 7 / s = 3 / a = 4 / b = 1 / fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
return = 14

n = 6 / s = 4 / a = 5 / b = 6 / fares = [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
return = 18
"""