num_list = [1, 2, 5, 3, 9, 6, 5, 3, 2]

stree = [0 for i in range(4*len(num_list))]

# 아무 함수나 와도 됨
def merge(left, right):
    return left + right

def build(stree, cur_node, left, right):
    if left == right:
        stree[cur_node] = num_list[left]
        return stree[cur_node]

    mid = left + (right + left)//2
    left_sum = build(stree, 2*cur_node, left, mid)
    right_sum = build(stree, 2*cur_node + 1, mid + 1, right)
    stree[cur_node] = merge(sum_left, sum_right)
    return stree[cur_node]

build(stree, 1, 0, len(num_list) - 1)

def query(start, end, node, left, right):
    if end < left or start > right:
        return 0

    if start <= left and right <= end:
        return stree[node]

    mid = left + (right - left)//2
    left_val = query(start, end, 2*node, left, mid)
    right_val = query(start, end, 2*node + 1, mid + 1, right)
    return merge(left_val, right_val)
