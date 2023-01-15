# A, B -> 비어있음 / C -> 가득
# 한 물통이 비거나 만대 가득찰 때까지 -> 물 손실 x

'''
주의
1. output : 세번 째 물통에 담겨있을 수 있는 물의 양을 모두 구해내는 프로그램
'''

import sys
from collections import defaultdict
A, B, C = map(int, sys.stdin.readline().split(' '))
visited = defaultdict(bool)
buk_A = [A, 0]
buk_B = [B, 0]
buk_C = [C, C]
answer_list = []
visited[(buk_A[1], buk_B[1], buk_C[1])] = True

# 마지막 set 시켜서 출력
# 중복 제거 -> visited -> dictionary로
def DFS(visited, A, B, C, answer_list):
    if not visited[(A[1], B[1], C[1])]:
        visited[(A[1], B[1], C[1])] = True
    else:
        return
    if A[1] == 0:
        answer_list.append(C[1])




DFS(visited, A, B, C, answer_list)