# 대기실 5개 각 대기실 5 * 5
# 맨해튼 거리 2이하 금지 -> 파티션은 ㄱㅊ
# table:0 응시자 : p 파티션 : x

from collections import deque


def solution(places):
    answer = []
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for place in places:
        possible = False
        p_loc = []
        for row in range(0, 5):
            for col in range(0, 5):
                if place[row][col] == "P":
                    p_loc.append([row, col])

        possible = True
        for row, col in p_loc:
            dq = deque()
            dq.append([row, col, 0])
            visited = [[row, col]]
            while dq:
                cur_row, cur_col, depth = dq.popleft()
                if place[cur_row][cur_col] == "P" and depth >= 1:
                    possible = False
                    break

                for add_row, add_col in move:
                    new_row, new_col = cur_row + add_row, cur_col + add_col
                    if new_row >= 5 or new_row < 0 or new_col >= 5 or new_col < 0:
                        continue
                    else:
                        if place[new_row][new_col] == "X":
                            continue
                        else:
                            if depth + 1 <= 2:
                                if [new_row, new_col] not in visited:
                                    visited.append([new_row, new_col])
                                    dq.append([new_row, new_col, depth + 1])
            if possible == False:
                break

        if possible == True:
            answer.append(1)
        else:
            answer.append(0)

    return answer