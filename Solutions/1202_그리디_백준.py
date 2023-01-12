# 보석 N (무게 Mi, 가격 Vi)
# 가방 K개 (최대 무게 Ci, 한개 보석만 가능)
# return 최대 가격

import sys
import heapq
N, K = map(int, sys.stdin.readline().rstrip().split(' '))

gem_list = []
for _ in range(N):
    gem_weight, gem_value = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    gem_list.append([gem_weight, gem_value, False])
gem_list = sorted(gem_list, key = lambda x : x[1], reverse = True)
q = []
for i in range(K):
    heapq.heappush(q, int(sys.stdin.readline().rstrip()))

num_of_gem = 0
cur_price = 0

while q:
    bag_weight = heapq.heappop(q)
    for i in range(len(gem_list)):
        gem_weight, gem_value, used = gem_list[i]
        if used == True:
            continue
        if gem_weight <= bag_weight:
            cur_price += gem_value
            num_of_gem += 1
            gem_list[i][2] = True
            break
    if num_of_gem == len(gem_list):
        break
print(cur_price)

