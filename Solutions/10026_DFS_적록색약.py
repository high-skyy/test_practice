# N*N RGB 구역의 수

import sys

N = int(sys.stdin.readline())
board = [ sys.stdin.readline().rstrip() for i in range(N) ]
# print(board)

check = [ [False for i in range(N)] for j in range(N) ]

d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]
num_not = 0
# 적록 색맹 x
for i in range(N):
    for j in range(N):
        if not check[i][j]:
            num_not += 1
            q = []
            q.append([i,j])
            cur_color = board[i][j]
            visited = [[i,j]]
            while q:
                cur_row, cur_col = q.pop(0)
                for k in range(4):
                    new_row = cur_row + d_row[k]
                    new_col = cur_col + d_col[k]
                    if new_row < 0 or new_row >= N or new_col < 0 or new_col >= N:
                        continue
                    if board[new_row][new_col] != cur_color:
                        continue
                    if [new_row, new_col] not in visited:
                        check[new_row][new_col] = True
                        visited.append([new_row, new_col])
                        q.append([new_row, new_col])

# 적록 색맹 o
num_yes = 0
for i in range(N):
    for j in range(N):
        check[i][j] = False
for i in range(N):
    for j in range(N):
        if not check[i][j]:
            num_yes += 1
            q = []
            q.append([i,j])
            cur_color = board[i][j]
            visited = [[i,j]]
            while q:
                cur_row, cur_col = q.pop(0)
                for k in range(4):
                    new_row = cur_row + d_row[k]
                    new_col = cur_col + d_col[k]
                    if new_row < 0 or new_row >= N or new_col < 0 or new_col >= N:
                        continue
                    if cur_color == 'R' or cur_color == 'G':
                        if board[new_row][new_col] == 'B':
                            continue
                    else:
                        if board[new_row][new_col] == 'R' or board[new_row][new_col] == 'G':
                            continue
                    if [new_row, new_col] not in visited:
                        check[new_row][new_col] = True
                        visited.append([new_row, new_col])
                        q.append([new_row, new_col])
print(f'{num_not} {num_yes}')