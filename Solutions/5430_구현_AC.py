# R -> 배열에 있는 수의 순서를 뒤집는 함수
# D -> 첫 번째 수를 버리는 함수 배열이 비어 있는데 D를 사용하는 경우 에러

# 배열 초기 값 + 수행할 함수

import sys

answer_list = []
num_TC = int(sys.stdin.readline())
for i in range(num_TC):
    error = False
    reverse = False
    func_list = list(sys.stdin.readline())
    func_list.pop(len(func_list) - 1)
    arr_length = int(sys.stdin.readline())
    temp = sys.stdin.readline().rstrip().lstrip('[').rstrip(']')
    if arr_length >= 1:
        arr = list(map(int, temp.split(',')))
    else:
        arr = []
    for command in func_list:
        if command == 'R':
            if arr_length <= 1:
                continue
            else:
                reverse = not reverse
        else:
            if arr_length <= 0:
                error = True
                print('error')
                break
            else:
                arr_length -= 1
                if reverse == True:
                    arr.pop(len(arr) - 1)
                else:
                    arr.pop(0)
    if not error:
        if reverse == True:
            temp = '['
            for i in range(arr_length - 1, -1, -1):
                temp += str(arr[i])
                temp += ','
            temp = temp.rstrip(',')
            temp += ']'
            print(temp)
        else:
            temp = '['
            for element in arr:
                temp += str(element)
                temp += ','
            temp = temp.rstrip(',')
            temp += ']'
            print(temp)


