# 어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때,
# 두 사람의 친구 네트워크에 몇 명이 있는지

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

TC_num = int(sys.stdin.readline())
TC_list = []
for _ in range(TC_num):
    num_relation = int(sys.stdin.readline())
    temp = []
    for i in range(num_relation):
        temp.append(list(sys.stdin.readline().rstrip().split(' ')))
    TC_list.append(temp)

answer_list = []

def find_parent(relation_dict, name):
    if name == relation_dict[name]['parent']:
        return name
    else:
        relation_dict[name]['parent'] = find_parent(relation_dict, relation_dict[name]['parent'])
        return relation_dict[name]['parent']

for TC in TC_list:
    relation_dict = defaultdict(dict)
    for left, right in TC:
        for i in [left, right]:
            if not relation_dict[i]:
                relation_dict[i]['parent'] = i
                relation_dict[i]['num'] = 1
        parent_of_left = find_parent(relation_dict, left)
        parent_of_right = find_parent(relation_dict, right)
        if parent_of_right == parent_of_left:
            answer_list.append(relation_dict[parent_of_left]['num'])
        else:
            relation_dict[parent_of_right]['parent'] = parent_of_left
            relation_dict[parent_of_left]['num'] += relation_dict[parent_of_right]['num']
            answer_list.append(relation_dict[parent_of_left]['num'])
for ans in answer_list:
    print(ans)