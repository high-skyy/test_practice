# N짜리 수열 -> 부분합 (합이 S 이상)


# input 받기
import sys
N, S = map(int, sys.stdin.readline().split(' '))
num_list = list(map(int, sys.stdin.readline().split(' ')))

'''
주의
1. 부분합이 0 보다 크다. (S > 0)
2. output : 최소 길이 출력 -> 불가능 : 0
3. 자연수 : 0 보다 크다.
'''

# double pointer
# 초기화
end_of_list = len(num_list)
start = 0
end = 0
min_length = end_of_list
sum = num_list[start]
found = False
while True:
    if sum >= S:
        found = True
        if min_length > end-start + 1:
            min_length = end-start + 1
        if start == end:
            start += 1
            end += 1
            if end >= end_of_list:
                break
            else:
                sum = num_list[end]
        else:
            start += 1
            sum -= num_list[start - 1]
    else:
        end += 1
        if end >= end_of_list:
            break
        else:
            sum += num_list[end]
if found:
    print(min_length)
else:
    print(0)