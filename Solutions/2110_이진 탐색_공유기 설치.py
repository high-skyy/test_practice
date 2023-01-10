# 수직선 N 개


# input 받기
import sys
N, C = map(int, sys.stdin.readline().split(' '))
house_loc = [int(sys.stdin.readline()) for _ in range(N)]

'''
주의
1. 여러개의 집이 같은 좌표 x
2. 공유기를 집에 설치 -> 하나만 가능 (2개 이상의 공유기 설치)
3. 가장 인접한 두 공유기 사이의 거리를 가능한 크게
'''

house_loc = sorted(house_loc)
min_offset = 1
max_offset = house_loc[len(house_loc) - 1] - house_loc[0]
answer = max_offset
while max_offset >= min_offset:
    count = 1
    mid_offset = (max_offset + min_offset) // 2
    sum = 0
    found = False
    for index in range(1, len(house_loc)):
        sum += house_loc[index] - house_loc[index - 1]
        if sum >= mid_offset:
            if sum == mid_offset:
                found = True
            sum = 0
            count += 1
    if count > C:
        min_offset = mid_offset + 1
    elif count < C:
        max_offset = mid_offset - 1
    else:
        if found:
            min_offset = mid_offset + 1
            answer = mid_offset
        else:
            min_offset = mid_offset + 1
print(answer)