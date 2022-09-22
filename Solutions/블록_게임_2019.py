# return -> 없앨 수 있는 블록 최대 개수
# board -> n*n 4<=n50<=
# board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],...

from collections import defaultdict
from collections import deque


def solution(board):
    answer = 0

    sequence = []
    dq = deque()
    block_dict = defaultdict(list)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]:
                block_dict[board[row][col]].append([row, col])
    # print(block_dict) {4: [[4, 6], [5, 5], [5, 6], [6, 6]], 3: [[6
    num_blocks = len(block_dict.keys())
    for key in block_dict.keys():
        temp = [block_dict[key]]
        temp.append(find_corners(block_dict[key], len(board[0])))
        dq.append(temp)

    count = 0
    while dq and len(dq) != count:
        locs, corners = dq.popleft()
        fill = [[row, col] for row in range(corners[0], corners[1] + 1) for col in range(corners[2], corners[3] + 1) if
                [row, col] not in locs]
        possible = []
        for point in fill:
            for row in range(point[0], -1, -1):
                if board[row][point[1]]:
                    possible.append(False)
                    break
                if row == 0:
                    possible.append(True)
        if possible == [True, True]:
            for loc in locs:
                board[loc[0]][loc[1]] = 0
            count = 0
        else:
            count += 1
            dq.append([locs, corners])
    answer = num_blocks - len(dq)

    return answer


def find_corners(block, n):
    row_min, row_max, col_min, col_max = [n + 1, -1, n + 1, -1]
    for loc in block:
        row, col = loc
        if row_min > row:
            row_min = row
        if row_max < row:
            row_max = row
        if col_min > col:
            col_min = col
        if col_max < col:
            col_max = col
    return [row_min, row_max, col_min, col_max]


"""
board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]
return = 2
"""