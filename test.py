# 4x4 격자 8가지의 캐릭터 (각 2장씩)
# 앞면 같으면 사라지고 아니면 원상복귀
# 1칸 이동 가장 가까운 카드 없으면 이동 x
# Enter -> +1 / 이동 -> +1

from collections import defaultdict
from itertools import permutations
from collections import deque


def solution(board, r, c):
    # board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
    answer = 0
    start_row, start_col = r, c
    # 위 오른 아래 왼
    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]

    friends_loc = defaultdict(list)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != 0:
                friends_loc[board[row][col]].append([row, col])

    result_dict = defaultdict(int)
    for perm in permutations(friends_loc.keys()):
        result_dict[perm] = 0

    for perm in result_dict:
        count = 0
        del_loc = []
        for friend in perm:
            loc_1, loc_2 = friends_loc[friend]
            target_dict = {tuple(loc_1): False, tuple(loc_2): False}

            dq = deque()
            dq.append([start_row, start_col, 0, target_dict])
            visited = []
            while dq:
                cur_row, cur_col, depth, target_dict = dq.popleft()
                # 조건 확인
                if list(target_dict.values()) == [True, True]:
                    del_loc.extend(target_dict.keys())
                    break
                new_target_dict = target_dict.copy()
                if (cur_row, cur_col) in new_target_dict:
                    new_target_dict[(cur_row, cur_col)] = True

                # 탐색
                for i in range(4):
                    new_row = cur_row + d_row[i]
                    new_col = cur_col + d_col[i]
                    if new_row <= 3 and new_row >= 0 and new_col <= 3 and new_col >= 0:
                        if [new_row, new_col] not in visited:
                            visited.append([new_row, new_col])
                            dq.append([new_row, new_col, depth + 1, new_target_dict])

                for i in range(4):
                    for mult in range(3, -1, -1):
                        new_row = cur_row + d_row[i]
                        new_col = cur_col + d_col[i]
                        if new_row <= 3 and new_row >= 0 and new_col <= 3 and new_col >= 0:
                            if [new_row, new_col] not in del_loc:
                                if [new_row, new_col] not in visited:
                                    visited.append([new_row, new_col])
                                    dq.append([new_row, new_col, depth + 1, new_target_dict])
                                    break

                count += depth
        result_dict[perm] += count

    answer = min(list(result_dict.values))
    return answer
solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)