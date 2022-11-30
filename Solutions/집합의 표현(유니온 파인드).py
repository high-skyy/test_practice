# 백준 집합의 표현



# n + 1 개의 집합

import sys
sys.setrecursionlimit(10**6)
n , m = map(int,sys.stdin.readline().split(' '))

command_list = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(m)]
union_list = [i for i in range(n+1)]

def find_root(union_list, index):
    if index == union_list[index]:
        return index
    else:
        union_list[index] = find_root(union_list, union_list[index])
        return union_list[index]

result_list = []

for mode, a, b in command_list:
    if mode == 0:
        if a == b:
            continue
        else:
            a_root = find_root(union_list, a)
            b_root = find_root(union_list, b)
            union_list[b_root] = a_root
    else:
        if a == b:
            result_list.append("YES")
        else:
            if find_root(union_list, a) == find_root(union_list, b):
                result_list.append("YES")
            else:
                result_list.append("NO")
for _ in result_list:
    print(_)



