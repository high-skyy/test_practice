# segment tree

num_list = [2,4,2,24,3,3,3,4,2,2]
seg_tree = [0 for i in range(len(num_list)* 4)]

def make_seg_tree(seg_tree, i, start, end):
    if start == end:
        seg_tree[i] = num_list[start]
        return seg_tree[i]

    mid = (start + end) //2
    seg_tree[i] = make_seg_tree(seg_tree, 2*i, start, mid) + make_seg_tree(seg_tree, 2*i + 1, mid + 1, end)
    return seg_tree[i]

def query_seg_tree(seg_tree, i, start_index, end_index, start, end):
    if start > end_index or end < start_index:
        print("return 0")
        return 0
    if start_index <= start and end <= end_index:
        print("found")
        return seg_tree[i]

    mid = (start + end) // 2
    return query_seg_tree(seg_tree, i * 2, start_index, end_index, start, mid) + query_seg_tree(seg_tree, i*2 + 1, start_index, end_index, mid + 1, end)

make_seg_tree(seg_tree, 1, 0, len(num_list)-1)
result = query_seg_tree(seg_tree, 1, 1, 5, 0, len(num_list) - 1)
print(result)
