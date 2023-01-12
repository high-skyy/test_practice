# 사과 먹으면 -> 뱀 길이 늘어남 벽 또는 자기자신과 부딪히면 게임 끝
# 뱀은 처음에 오른쪽 향함 N*N 정사각 보드

# 먼저 몸길이를 늘려 머리를 다음칸 -> 사과 o 꼬리 그대로 사과 x 꼬리 위치 칸 끝내자.

import sys
from collections import defaultdict

# Get input
N = int(sys.stdin.readline())
num_apple = int(sys.stdin.readline())
apple_loc = defaultdict(bool)
for i in range(num_apple):
    row, col = list(map(int,sys.stdin.readline().split(' ')))
    apple_loc[(row-1, col-1)] = True
num_turn = int(sys.stdin.readline())
turn_list = [list(sys.stdin.readline().rstrip().split(' ')) for i in range(num_turn)]
# print(length)
# print(apple_loc)
# print(turn_list)

cur_time = 0
cur_row = 0
cur_col = 0
bam_loc = [[0,0]]
board = [[False for i in range(N)] for j in range(N)]
board[0][0] = True
cur_dir = 0
dir_dict = {}
dir_dict[0] = [0,1]
dir_dict[1] = [1,0]
dir_dict[2] = [0, -1]
dir_dict[3] = [-1, 0]
if turn_list:
    next_turn_time, next_turn_dir = turn_list.pop(0)
    next_turn_time = int(next_turn_time)
else:
    next_turn_time = -1

while True:
    cur_time += 1
    cur_row += dir_dict[cur_dir][0]
    cur_col += dir_dict[cur_dir][1]
    if cur_row < 0 or cur_row >= N or cur_col < 0 or cur_col >= N:
        break
    if board[cur_row][cur_col]:
        break
    if next_turn_time == cur_time:
        if next_turn_dir == 'D':
            cur_dir = (cur_dir + 1) % 4
        else:
            cur_dir = (cur_dir - 1 + 4) % 4
        if turn_list:
            next_turn_time, next_turn_dir = turn_list.pop(0)
            next_turn_time = int(next_turn_time)
        else:
            next_turn_time = -1
    board[cur_row][cur_col] = True
    bam_loc.append([cur_row, cur_col])
    if apple_loc[(cur_row, cur_col)] == True:
        apple_loc[(cur_row, cur_col)] = False
    else:
        del_row, del_col = bam_loc.pop(0)
        board[del_row][del_col] = False
print(cur_time)

