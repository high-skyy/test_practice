# 백준 나무 심기

import sys

N = int(sys.stdin.readline())
coord_list = [int(sys.stdin.readline()) for _ in range(N)]

result = 1

seg_tree = [0 for _ in range(len(coord_list)*4)]

def make_tree(seg_tree,node, start, end):
    if start == end:
        seg_tree[node] = coord_list[start]
        return seg_tree[node]
    mid = (start + end) // 2
    seg_tree[node] = make_tree(seg_tree, node * 2, start, mid) + make_tree(seg_tree, node*2 + 1, mid + 1, end)
    return seg_tree[node]

def query_tree(seg_tree, node, left, right, start, end, cur_loc):
    if left > end or right < start:
        return 0

    if start <= left and right <= end:
        return abs(seg_tree[node] - cur_loc)
    mid = (start + end) // 2
    seg_tree[node] = query_tree(seg_tree, node * 2, left, right, start, mid, cur_loc) + query_tree(seg_tree, node * 2 + 1, left, right, mid + 1, end, cur_loc)
    return seg_tree[node]

make_tree(seg_tree, 1, 0, len(coord_list) - 1)

for i in range(0, len(coord_list)):
    if i == 0:
        continue
    total_dist = 0
    cur_loc = coord_list[i]

    total_dist = query_tree(seg_tree, 1, 0, i-1, 0, len(coord_list) - 1, cur_loc)
    result *= total_dist

print(result % 1000000007)