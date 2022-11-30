# 세그먼트

# a번째 정수부터 b번재 정수까지 제일 작은 정수
import sys
N, M = map(int, sys.stdin.readline().split(' '))
num_list = [int(sys.stdin.readline()) for i in range(N)]
query_list = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(M)]

seg_min_tree = [0 for _ in range(len(num_list) * 4)]
seg_max_tree = [0 for _ in range(len(num_list) * 4)]
def make_tree(seg_tree, node, start, end, mode):
    if start == end:
        seg_tree[node] = num_list[start]
        return num_list[start]
    mid = (start + end) // 2
    if mode == 'min':
        seg_tree[node] = min(make_tree(seg_tree, node*2, start, mid, 'min') , make_tree(seg_tree, node*2 + 1, mid+1, end, 'min'))
    else:
        seg_tree[node] = max(make_tree(seg_tree, node * 2, start, mid, 'max'), make_tree(seg_tree, node * 2 + 1, mid + 1, end, 'max'))
    return seg_tree[node]

make_tree(seg_min_tree, 1, 0, len(num_list)-1, 'min')
make_tree(seg_max_tree, 1, 0, len(num_list)-1, 'max')

def query_tree(seg_tree, node, left, right, start, end, mode):
    if end < left or right < start:
        if mode == 'min':
            return 1000000001
        else:
            return 0

    if left <= start and end <= right:
        return seg_tree[node]
    mid = (start + end) // 2
    if mode == 'min':
        return min(query_tree(seg_tree, node*2, left, right, start, mid, mode), query_tree(seg_tree, node*2 + 1, left, right, mid + 1, end, mode))
    else:
        return max(query_tree(seg_tree, node*2, left, right, start, mid, mode), query_tree(seg_tree, node*2 + 1, left, right, mid + 1, end, mode))

for left, right in query_list:
    min_value = query_tree(seg_min_tree, 1, left-1, right-1, 0, len(num_list)-1, 'min')
    max_value = query_tree(seg_max_tree, 1, left-1, right-1, 0, len(num_list)-1, 'max')
    print(f'{min_value} {max_value}')