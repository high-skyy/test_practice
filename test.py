# 3 연산 문자 (+, -, *) 우선순위 -> 큰 숫자
# 계산된 결과가 음수 -> 절댓 값

from itertools import permutations
import re


def solution(expression):
    answer = 0
    # 연산자 순서대로 (permutations)
    # "100-200*300-500+20"
    operand_list = list(map(int, re.findall("[0-9]+", expression)))
    operator_list = re.findall("[\W]", expression)
    new_list = [operand_list[0]]
    for i in range(len(operator_list)):
        new_list.append(operator_list[i])
        new_list.append(operand_list[i])
    # print(new_list)
    max_value = 0
    for op_seq in permutations(operator_list):
        test_list = new_list[:]
        for op in op_seq:
            while op in test_list:
                index = test_list.index(op)
                first = test_list.pop(index - 1)
                second = test_list.pop(index - 1)
                third = test_list.pop(index - 1)
                if op == "-":
                    test_list.insert(index - 1, first - third)
                elif op == "+":
                    test_list.insert(index - 1, first + third)
                else:
                    test_list.insert(index - 1, first * third)
            print(test_list)
        if test_list[0] > max_value:
            max_value = test_list[0]
    return max_value
solution("100-200*300-500+20")