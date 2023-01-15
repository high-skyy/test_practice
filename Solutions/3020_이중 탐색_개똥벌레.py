# 동굴의 길이 N미터, 높이는 H미터
# 종유석 석순 번갈아

import sys

N, H = map(int, sys.stdin.readline().rstrip().split(' '))
cur = 1
sum_list = [0 for _ in range(H + 2)]
for _ in range(N):
    height = int(sys.stdin.readline())
    if cur == 1:
        sum_list[1] += 1
        sum_list[height + 1] -= 1
    else:
        sum_list[len(sum_list) - 1 - height] += 1
        sum_list[len(sum_list) - 1] -= 1
    cur *= (-1)
for i in range(H + 1):
    sum_list[i+1] += sum_list[i]
min_destroy = N + 1
count = 0
for index in range(1, H + 1):
    if sum_list[index] == min_destroy:
        count += 1
    elif sum_list[index] < min_destroy:
        count = 1
        min_destroy = sum_list[index]
print(min_destroy, count)