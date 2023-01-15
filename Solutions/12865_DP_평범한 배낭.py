# N개 물건 -> 무게 W 가치 V
# 가방 최대 K 만큼의 무게
'''
주의
1. 가치의 최댓 값 반환
2. 모두 정수
'''

import sys
N, K = map(int, sys.stdin.readline().split(' '))
item_list = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
DP = [[0 for i in range(K+1)] for j in range(N+1)]
for j in range(len(item_list)):
    weight, value = item_list[j]
    for bag_weight in range(K+1):
        if bag_weight - weight < 0:
            DP[j+1][bag_weight] = DP[j][bag_weight]
        else:
            DP[j+1][bag_weight] = max(DP[j][bag_weight], DP[j][bag_weight - weight] + value)
print(DP[N][K])