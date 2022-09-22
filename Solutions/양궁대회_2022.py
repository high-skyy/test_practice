from itertools import combinations_with_replacement
import copy


def solution(n, info):
    answer = []
    global answer_list
    global max_diff
    answer_list = []
    max_diff = 1
    for every_combination in combinations_with_replacement([i for i in range(11)], n):
        trans_list = [0 for j in range(11)]
        for i in range(11):
            trans_list[10 - i] = every_combination.count(i)
        calculate(list(trans_list), info)
    # print("max_diff is : ", max_diff)
    # print("answer_list is : ", answer_list)

    if len(answer_list) == 0:
        return [-1]
    elif len(answer_list) == 1:
        answer = answer_list[0]
    else:
        answer = find_answer()

    return answer


def find_answer():
    global answer_list
    answer = []
    for index in range(11):
        num = 0
        max_value = -1
        for every_answer in answer_list:
            if every_answer[10 - index] > max_value:
                num = 1
                max_value = every_answer[10 - index]
                answer = every_answer
            elif every_answer[10 - index] == max_value:
                num = num + 1
            else:
                continue
        if num == 1:
            return answer
        else:
            continue


def calculate(trans_list, info):
    global answer_list
    global max_diff
    apeach_score = 0
    ryan_score = 0
    for i in range(11):
        if info[i] == 0 and trans_list[i] == 0:
            continue
        else:
            if info[i] >= trans_list[i]:
                apeach_score = apeach_score + 10 - i
            else:
                ryan_score = ryan_score + 10 - i
    difference = ryan_score - apeach_score
    if max_diff < difference:
        max_diff = difference
        answer_list.clear()
        answer_list.append(trans_list)
    elif max_diff == difference:
        answer_list.append(trans_list)


"""
n = 5
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
return = [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]

n = 1
info = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
retrun = [-1]

n = 9
info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
return = [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]

n = 10
info = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]
return = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]
"""