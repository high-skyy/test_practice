# 자물쇠 -> 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태
# 열쇠는 M x M 크기인 정사각 격자 형태
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만
# 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다
# key [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	lock [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# 0은 홈 부분, 1은 돌기 부분

from collections import defaultdict


def solution(key, lock):
    answer = False
    M, N = len(key), len(lock)
    key_pos = [[i, j] for i in range(M) for j in range(M) if key[i][j]]  # [i, 0, 0, j]
    # print(key_pos) 	[[1, 0], [2, 1], [2, 2]]
    lock_pos = sorted([[i, j] for i in range(N) for j in range(N) if lock[i][j] == 0])
    if len(lock_pos) == 0:
        return True
    # 하좌상우 [1, 0, 0, 0] -> [0, 1, 0, 0]
    move = [[0, 1, 1, 1], [1, 1, 0, -1], [0, -1, 1, -1], [1, -1, 0, 1]]
    end_point = [[0, 0], [0, M - 1], [M - 1, M - 1], [M - 1, 0]]
    for r in range(-(N - 1), N):
        for c in range(-(N - 1), N):
            for i in range(4):  # 회전
                bench = end_point[i]
                mv = move[i]
                test = []
                debug = []
                debug_1 = []
                for point in key_pos:
                    row = bench[0] + point[mv[0]] * mv[1] + r
                    col = bench[1] + point[mv[2]] * mv[3] + c
                    if row >= 0 and row < N and col >= 0 and col < N:
                        test.append([row, col])
                    else:
                        continue
                if len(test) == len(lock_pos):
                    if sorted(test) == lock_pos:
                        return True

    return answer
solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
"""
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
"""

