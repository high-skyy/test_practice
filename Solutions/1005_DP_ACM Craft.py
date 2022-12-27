# 건물 짓는 순서가 주어진다. 건설 시간 존재

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def find_time(end, tree, time_list):
    if tree[end]["time"] == -1:
        if tree[end]["child"]:
            tree[end]["time"] = max([find_time(new_end, tree, time_list) for new_end in tree[end]["child"]]) + time_list[end]
        else:
            tree[end]["time"] = time_list[end]
    return tree[end]["time"]

num_TC = int(sys.stdin.readline())
print_list = []
for _ in range(num_TC):
    num_building, num_order = list(map(int, sys.stdin.readline().split(' ')))
    build_time_list = list(map(int, sys.stdin.readline().split(' ')))
    build_time_list.insert(0,-1)
    tree = defaultdict(dict)
    for i in range(num_building):
        tree[i + 1]["time"] = -1
        tree[i + 1]["child"] = []
    for i in range(num_order):
        first, second = list(map(int, sys.stdin.readline().split(' ')))
        tree[second]["child"].append(first)
    victory_building = int(sys.stdin.readline())

    # 해당 TC에 대해서
    max_time = find_time(victory_building, tree, build_time_list)
    print_list.append(max_time)
for result in print_list:
    print(result)


