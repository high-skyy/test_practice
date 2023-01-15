# 서로 다른 L개의 알파벳 소문자 (모음 최소 1개 / 최소 두 개의 자음)
# C개의 문자 주어짐

# input 받기
import sys
from itertools import combinations
from itertools import permutations
L, C = map(int, sys.stdin.readline().rstrip().split(' '))
alpha_list = sys.stdin.readline().rstrip().split(' ')

# 자음 모음 나눠서 combination 만들고 순열 (x) -> 여 집합 활용
vowel = ['a', 'e', 'i', 'o', 'u']
answer_list = []
for comb in combinations(alpha_list, L):
    num = 0
    for alpha in comb:
        if alpha in vowel:
            num += 1
    if num >= 1 and L - num >= 2:
        comb_list = list(comb)
        comb_list.sort()
        answer_list.append(''.join(comb_list))
answer_list.sort()

for entry in answer_list:
    print(entry)

