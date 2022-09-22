# board의 한 변의 길이는 5이상 100 이하
# board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

from collections import deque


def solution(board):
    answer = 0

    visited = []
    cur = [[0, 0], [0, 1]]
    dq = deque()
    dq.append([cur, 0])
    length = len(board)
    visited.append(cur)

    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]
    rot = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while dq:
        cur, depth = dq.popleft()
        if cur[0] == [length - 1, length - 1] or cur[1] == [length - 1, length - 1]:
            answer = depth
            break
        for i in range(4):
            count = 0
            next_pos = []
            for point in cur:
                trans_point = [point[0] + d_row[i], point[1] + d_col[i]]
                if check_pos(board, trans_point, visited):
                    next_pos.append(trans_point)
                else:
                    break
            # print(next_pos)
            if len(next_pos) == 2:
                next_pos = sorted(next_pos)
                if next_pos not in visited:
                    visited.append(next_pos)
                    dq.append([next_pos, depth + 1])
        # print("dq after move : ", dq)
        # 회전       U       R       D        L
        # rot = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        row_1, col_1 = cur[0]
        row_2, col_2 = cur[1]
        check_list = []
        if row_1 == row_2:
            check_list.append([cur[0], 1])
            check_list.append([cur[1], 3])
        elif col_1 == col_2:
            check_list.append([cur[0], 2])
            check_list.append([cur[1], 0])
        check_three = []
        for check in check_list:
            trans_list_c = [check[0]]
            trans_list_cc = [check[0]]
            clock = [check[0][0] + rot[(check[1] + 1) % 4][0], check[0][1] + rot[(check[1] + 1) % 4][1]]
            counter = [check[0][0] + rot[(check[1] + 3) % 4][0], check[0][1] + rot[(check[1] + 3) % 4][1]]
            trans_list_c.append(clock)
            trans_list_cc.append(counter)
            if check[1] % 2 == 1:
                # 돈 후 row 돌기 전 col
                trans_list_c.append([clock[0], check[0][1] + rot[check[1]][1]])
                trans_list_cc.append([counter[0], check[0][1] + rot[check[1]][1]])
            else:
                trans_list_c.append([check[0][0] + rot[check[1]][0], clock[1]])
                trans_list_cc.append([check[0][0] + rot[check[1]][0], counter[1]])
            check_three.append(trans_list_c)
            check_three.append(trans_list_cc)
        for ch in check_three:
            count = 0
            for point in ch[1:3]:
                if check_pos(board, point, visited):
                    count += 1
                else:
                    break
            if count == 2:
                new_pos = sorted([ch[0], ch[1]])
                if new_pos not in visited:
                    visited.append([ch[0], ch[1]])
                    dq.append([[ch[0], ch[1]], depth + 1])

    return answer


def check_pos(board, point, visited):
    length = len(board)
    if point[0] < length and point[0] >= 0 and point[1] < length and point[1] >= 0:
        if board[point[0]][point[1]] == 0:
            return True
    return False

"""
board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
result = 7
"""
