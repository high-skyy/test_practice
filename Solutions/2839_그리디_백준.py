# 설탕을 정확하게 N킬로그램 배달
# 3 봉지 / 5봉지
# 정확하게 N킬로그램 만들 수 없으면 -1 출력
import sys
N = int(sys.stdin.readline().rstrip())

def solution(N):
    num_bong = 0
    max_bong5_num = N // 5
    for num in range(max_bong5_num, -1, -1):
        cur = N - num*5
        if cur % 3 != 0:
            continue
        return print(num + (cur // 3))
    return print(-1)
solution(N)
