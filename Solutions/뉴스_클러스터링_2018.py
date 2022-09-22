"""
유사한 기사를 묶는 기준을 정하기 위해서 논문과 자료를 조사하던 튜브는 "자카드 유사도"라는 방법을 찾아냈다.
"""
#  두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.
# 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
# 다중 집합 합집합은 겹치는 원소의 max 기준 교 집합은 min 기준
# 두 글자씩 끊어서 다중집합의 원소로 만든다
# , 대문자와 소문자의 차이는 무시한다. "AB"와 "Ab", "ab"는 같은 원소로 취급한다.
import re


def solution(str1, str2):
    answer = 0
    # data cleaning
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = re.sub(r"[^a-z]", ' ', str1)
    str2 = re.sub(r"[^a-z]", ' ', str2)

    # 집합 만들기
    str1_set = make_set(str1)
    str2_set = make_set(str2)

    # 검사
    test_set = []
    for every_element in str1_set:
        for every_element_2 in str2_set:
            if every_element == every_element_2:
                test_set.append(every_element)
    print(set(test_set))
    # 최대 최소 갯수 구하기
    union_num = len(str1_set) + len(str2_set)
    and_num = 0
    for every_element in set(test_set):
        num1 = check_number(every_element, str1_set)
        num2 = check_number(every_element, str2_set)
        union_num = union_num - num1 - num2 + max(num1, num2)
        and_num = and_num + min(num1, num2)
    if union_num == 0:
        answer = 65536
    else:
        answer = int(float(and_num) * 65536 / float(union_num))
    print(answer)

    return answer


def make_set(str_num):
    result = []
    for i in range(len(str_num)):
        j = i + 1
        if j < len(str_num):
            if str_num[i] != ' ' and str_num[j] != ' ':
                trans = ''
                trans = trans + str_num[i]
                trans = trans + str_num[j]
                result.append(trans)
    return result


def check_number(element, test_list):
    num = 0
    for every_thing in test_list:
        if every_thing == element:
            num = num + 1
    return num

"""
str1 = "FRANCE" / str2 = "french" / return = 16384
str1 = "handshake" / str2 = "shake hands" / return = 65536
str1 = "aa1+aa2" / str2 = "AAAA12" / return 43690
str1 = "E=M*C^2" / str2 = "e=m*c^2" / return 65536

"""