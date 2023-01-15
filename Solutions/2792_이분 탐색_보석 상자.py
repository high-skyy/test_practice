# 색상 : M 가지 -> N명의 학생
# 질투심 : 보석 많은 학생ㅇ이 가지고 있는 보석의 개수 -> 최소화
'''
주의
1. 항상 같은 색상의 보석을 가져감
2. output : 최소 질투심
'''
# input 받기
import sys
N, M = map(int, sys.stdin.readline().split(' '))
gem_list = [int(sys.stdin.readline()) for _ in range(M)]
start = 1
end = max(gem_list)
answer = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for num in gem_list:
        if num % mid == 0:
            count += (num // mid)
        else:
            count += (num // mid) + 1
    if count > N:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1
print(answer)

