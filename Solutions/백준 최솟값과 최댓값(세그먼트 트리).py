#

N, M = map(int, input().split(' '))
num_list = [int(input()) for _ in range(N)]
a_b_list = [list(map(int, input().split(' '))) for _ in range(M)]

seg_tree = [i for i in range(len(num_list) * 4)]

def make_tree(seg_tree, num_list, start, end):
    mid = (start + end) // 2



