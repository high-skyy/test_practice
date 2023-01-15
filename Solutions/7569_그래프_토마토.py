# 익은 토마토 -> 익지 않은 토마토 영향
# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
# 최소 일수
'''
주의
1. 익 : 1, 익 x : 0, -1 : no tomato
2. output : 처음부터 다 익으면 0 / 다 익지 못하면 -1
'''

import sys
col_len, row_len, height_len = map(int, sys.stdin.readline().split(' '))
box = [[list(map(int, sys.stdin.readline().split(' '))) for i in range(row_len)] for k in range(height_len)]
not_ripe_num = 0
for height in range(height_len):
    for row in range(row_len):
        for col in range(col_len):
            if box[height][row][col] == 0:
                not_ripe_num += 1
# 익지 않은 것의 갯수 변화 x -> -1 을 출력한다.
# 익지 않은 것 기준
# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
d_height = [-1, 1, 0, 0, 0, 0]
d_row = [0, 0, 0, 0, 1, -1]
d_col = [0, 0, -1, 1, 0, 0]
possible = True
if not_ripe_num == 0:
    print(0)
else:
    time = 0
    while True:
        change = False
        check_list = []
        for height in range(height_len):
            for row in range(row_len):
                for col in range(col_len):
                    if box[height][row][col] == 1 or box[height][row][col] == -1:
                        continue
                    else:
                        for i in range(6):
                            new_height = height + d_height[i]
                            new_row = row + d_row[i]
                            new_col = col + d_col[i]
                            if new_height < 0 or new_height >= height_len or new_row < 0 or new_row >= row_len or new_col < 0 or new_col >= col_len:
                                continue
                            if box[new_height][new_row][new_col] == 1:
                                change = True
                                check_list.append([height, row, col])
                                not_ripe_num -= 1
                                break
        for height, row, col in check_list:
            box[height][row][col] = 1
        if change:
            time += 1
            if not_ripe_num == 0:
                break
        else:
            possible = False
            break
    if possible:
        print(time)
    else:
        print(-1)

