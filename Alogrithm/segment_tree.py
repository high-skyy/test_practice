from collections import defaultdict
num_list = [1, 2, 5, 3, 9, 6, 5, 3, 2]
seg_tree = [0 for i in range(2**len(num_list)*2)]
# log (len(num_list)) ceiling 씌우고 2**

def make_seg_tree (start, end, cur_node, num_list, seg_tree):
    if start == end:
        seg_tree[cur_node] = num_list[start]
        return num_list[start]

    mid = (start + end) // 2
    left_sum = make_seg_tree(start, mid, cur_node*2, num_list, seg_tree)
    right_sum = make_seg_tree(mid+1, end, cur_node*2 + 1, num_list, seg_tree)
    seg_tree[cur_node] = left_sum + right_sum
    return left_sum + right_sum

make_seg_tree(0, len(num_list) - 1, 1, num_list, seg_tree)

def find_value(start_index, end_index, cur_node, start_tree, end_tree, stree):
    if start_index <= start_tree and end_tree <= end_index:
        return stree[cur_node]
    elif end_index < start_tree or start_index > end_tree:
        return 0

    mid = (start_tree + end_tree)//2
    left_sum = find_value(start_index, end_index, cur_node * 2, start_tree, mid, stree)
    right_sum = find_value(start_index, end_index, cur_node * 2 + 1, mid + 1, end_tree, stree)
    return left_sum + right_sum

def update(index, val, node, left, right):
    if index < left or index > right:
        return seg_tree[node]

    if left == right:
        seg_tree[node] = val
        return seg_tree[node]

    mid = (left + right) //2
    left_val = update(index, val, 2*node, left, mid)
    right_val = update(index, val, 2*node + 1, mid + 1, right)
    seg_tree[node] = left_val + right_val
    return seg_tree[node]

print(find_value(4, 7, 1, 0, len(num_list)-1 , seg_tree))
print("here")
update(3, 100, 1, 0, len(num_list) - 1)
print(seg_tree[1])