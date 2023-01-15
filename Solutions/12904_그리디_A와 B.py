# 두 문자열 S, T
# 문자열의 뒤에 A를 추가한다. 문자열을 뒤집고 뒤에 B를 추가한다.
'''
주의
1. S의 길이 < T의 길이
2. output : 바꿀 수 있으면 1 없으면 0을 출력
'''
import sys
S = list(sys.stdin.readline().rstrip())
T = list(sys.stdin.readline().rstrip())
len_T = len(T) - 1
len_S = len(S) - 1
while len_T > len_S:
    cur = T.pop(len_T)
    if cur == 'B':
        T = T[::-1]
    len_T = len(T) - 1
if T == S:
    print(1)
else:
    print(0)