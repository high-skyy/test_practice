# N*N
board = [[]]
'''
주의
1. N은 3^^k
'''
# input 받기
import sys
N = int(sys.stdin.readline())



# 초기 initialize 이후 -> 빈칸만 찾아서 바꾸기
# Initialize
tmp = ''
for _ in range(N):
    tmp += '*'
board = [['*' for i in range(N)] for j in range(N)]

def change_board(board, N, cur_row, cur_col):
    offset = N // 3
    if offset == 0:
        return
    row_start = cur_row + offset
    col_start = cur_col + offset
    for row in range(row_start, row_start + offset):
        for col in range(col_start, col_start + offset):
            board[row][col] = ' '
    for add_row in range(3):
        for add_col in range(3):
            change_board(board, offset, cur_row + add_row*offset, cur_col + add_col*offset)


change_board(board, N, 0, 0)
for line in board:
    print(''.join(line))