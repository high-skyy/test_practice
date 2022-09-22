# 모든 노드는 서로 다른 x값을 가진다.
# 같은 레벨(level)에 있는 노드는 같은 y 좌표를 가진다.
# [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

import heapq
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)


def solution(nodeinfo):
    answer = []

    temp_list = []

    tree = defaultdict(dict)
    count = 1
    for node in nodeinfo:
        heapq.heappush(temp_list, [-node[1], node[0], count])
        count += 1
    while temp_list:
        if not tree.keys():
            root = heapq.heappop(temp_list)
            root_node = [root[1], -root[0], root[2]]
            tree["V"] = root_node
        else:
            temp_node = heapq.heappop(temp_list)
            next_node = [temp_node[1], -temp_node[0], temp_node[2]]
            make_tree(next_node, root_node, tree, temp_list)
    for sequence in [["V", "L", "R"], ["L", "R", "V"]]:
        answer.append(traverse_tree(tree, sequence, []))
    return answer


def traverse_tree(tree, sequence, result):
    for seq in sequence:
        if seq == "V":
            result.append(tree[seq][2])
        else:
            if tree[seq]:
                traverse_tree(tree[seq], sequence, result)
            else:
                continue
    return result


def make_tree(next_node, prev_node, tree, temp_list):
    if next_node[0] < prev_node[0]:  # 왼쪽 sub_tree
        if tree["L"]:  # 이미 있으면
            make_tree(next_node, tree["L"]["V"], tree["L"], temp_list)
        else:
            tree["L"] = defaultdict(dict)
            tree["L"]["V"] = next_node
    elif next_node[0] > prev_node[0]:
        if tree["R"]:  # 이미 있으면
            make_tree(next_node, tree["R"]["V"], tree["R"], temp_list)
        else:
            tree["R"] = defaultdict(dict)
            tree["R"]["V"] = next_node

"""
nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
return = [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
"""