#

import sys
from collections import defaultdict

# input 받기
passwd_string = sys.stdin.readline().strip()
letter_dict = defaultdict(str)

num_list = [str(i) for i in range(1, 27)]
letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I' ,'J', 'K', 'L', 'M', 'N', 'O' ,'P','Q','R','S','T','U','V','W','X','Y','Z']

for num, letter in zip(num_list, letter_list):
    letter_dict[num] = letter

DP = [0 for i in range(len(passwd_string))]
# initialize

if len(passwd_string) == 0:
    print(0)
elif len(passwd_string) == 1:
    if passwd_string[0] in letter_dict:
        print(1)
    else:
        print(0)
elif len(passwd_string) == 2:
    if passwd_string[0] in letter_dict:
        DP[0] = 1
    if passwd_string[1] in letter_dict:
        DP[1] += DP[0]
    if passwd_string[0:2] in letter_dict:
        DP[1] += 1
    print(DP[len(DP) - 1] % 1000000)
else:
    if passwd_string[0] in letter_dict:
        DP[0] = 1
    if passwd_string[0] in letter_dict:
        DP[0] = 1
    if passwd_string[1] in letter_dict:
        DP[1] += DP[0]
    if passwd_string[0:2] in letter_dict:
        DP[1] += 1
    for index in range(2, len(passwd_string)):
        if passwd_string[index - 1:index + 1] in letter_dict:
            # print(f'2 : {passwd_string[index - 1:index + 1]}')
            DP[index] += DP[index - 2]
        if passwd_string[index] in letter_dict:
            # print(f'2 : {passwd_string[index]}')
            DP[index] += DP[index - 1]
        DP[index] = DP[index] % 1000000
    print(DP[len(DP) - 1])