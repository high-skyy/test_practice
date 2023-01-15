# 세로 : R / 가로 C -> 보드 / 상하좌우 이동 말 시작 : 1행 1열
# 새로운 알파벳만 지나와야 함

# input 받기
import sys
from collections import defaultdict
R, C = map(int, sys.stdin.readline().split(' '))
board = [ list(sys.stdin.readline().rstrip().strip()) for _ in range(R) ]
sys.setrecursionlimit(10**6)
'''
주의
1. 행열 1부터 시작 (0 아님)
2. 좌측 상단도 포함
'''

# DFS (BFS 보다 더 효율적일 가능성이 높음)
alpha_dict = defaultdict(int)
cnt = 0
for alpha in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y','Z']:
    alpha_dict[alpha] = cnt
    cnt += 1
for row in range(R):
    for col in range(C):
        board[row][col] = alpha_dict[board[row][col]]
visited = [False for _ in range(26)]
cur_row = 0
cur_col = 0
d_row = [1, 0, -1, 0]
d_col = [0, 1, 0, -1]
global max_depth
max_depth = 1
def DFS(board, visited, depth, cur_row, cur_col):
    global max_depth
    if visited[board[cur_row][cur_col]]:
        return
    else:
        visited[board[cur_row][cur_col]] = True
    if depth > max_depth:
        max_depth = depth
    for i in range(4):
        new_row = cur_row + d_row[i]
        new_col = cur_col + d_col[i]
        if new_row < 0 or new_row >= R or new_col < 0 or new_col >= C:
            continue
        else:
            DFS(board, visited, depth + 1, new_row, new_col)
    visited[board[cur_row][cur_col]] = False
DFS(board, visited, 1, cur_row, cur_col)
print(max_depth)