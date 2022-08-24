# 같은 값 연속 -> 문자 개수와 반복되는 값으로 표현
# 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return


def solution(s):
    answer = 0

    # s = "aabbaccc"
    #      01234567
    min_value = len(s)
    result = ""
    for i in range(1, int(len(s) / 2) + 1):
        temp = ""
        count = 0
        for j in range(0, len(s), i):
            if s[j:j + i] == s[j + i:j + 2 * i]:
                count += 1
            else:
                if count >= 1:
                    temp += str(count + 1)
                    temp += s[j:j + i]
                    count = 0
                else:
                    count = 0
                    temp += s[j:j + i]
        if count >= 1:
            temp += str(count + 1)
            temp += s[j:j + i]
        if min_value > len(temp):
            min_value = len(temp)
    answer = min_value
    print(answer)
    return answer
solution("aabbacc")
"""
test - case
s = "aabbaccc" return 7
s = "ababcdcdababcdcd" return 9
s = "abcabcdede" return 8
s = "abcabcabcabcdededededede" return 14
s = "xababcdcdababcdcd" return 17
"""