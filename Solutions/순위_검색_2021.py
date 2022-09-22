# 개발언어 cpp, java, python 지원 직군 backend와 frontend 경력구분 junior와 senior 중 하나를 선택 소울푸드로 chicken과 pizza 중 하나를 선택
# [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
# info -> "개발언어 직군 경력 소울푸드 점수" -> 문자열 query(문의 조건) java and backend and junior and pizza 100"
# 문의 조건에 해당 하는 사람들의 숫자를 순서대로 배열에 담아 return 하도록 solution 함수 완성
from collections import defaultdict


def solution(info, query):
    answer = []
    table = defaultdict(list)

    for every_information in info:
        lang, b_f, exp, food, score = every_information.split(' ')
        tuple_list = make_tuple(lang, b_f, exp, food)
        for every_tuple in tuple_list:
            table[every_tuple].append(int(score))
    # print(table)

    for every_key in table.keys():
        table[every_key] = sorted(table[every_key], reverse=True)

    for every_query in query:
        every_query = every_query.replace("and ", "")
        lang, b_f, exp, food, score = every_query.split(' ')
        # print("every_information is : ", every_information)
        num = find_num(table[tuple([lang, b_f, exp, food])], int(score))
        answer.append(num)

    return answer


def find_num(find_list, threshold):
    left = 0
    right = len(find_list)
    while left - right < 0:
        middle = int((left + right) / 2)
        if find_list[middle] >= threshold:
            left = middle + 1
        else:
            right = middle
    return left


def make_tuple(lang, b_f, exp, food):
    result = []
    for i in [lang, "-"]:
        trans = []
        trans.append(i)
        for j in [b_f, "-"]:
            trans.append(j)
            for k in [exp, "-"]:
                trans.append(k)
                for l in [food, "-"]:
                    trans.append(l)
                    result.append(tuple(trans))
                    del trans[3]
                del trans[2]
            del trans[1]
        del trans[0]
    return result


"""
info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
return = [1, 1, 1, 1, 2, 4]
"""