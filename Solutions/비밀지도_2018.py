# 하나라도 벽 -> 전체에서 벽
# arr1 = [9, 20, 28, 18, 11], arr2 = [30, 1, 21, 17, 28]


def solution(n, arr1, arr2):
    answer = []

    board = [[0 for i in range(n)] for j in range(n)]

    # 2 진수로 바꾸고
    for arr in [arr1, arr2]:
        for row in range(len(arr)):
            cur = arr[row]
            col = n - 1
            while cur > 0:
                if cur % 2 == 1:
                    board[row][col] = 1
                    cur -= 1
                    cur = cur / 2
                    col -= 1
                else:
                    cur = cur / 2
                    col -= 1
    for row in board:
        text = ''
        for loc in row:
            if loc == 1:
                text += '#'
            else:
                text += ' '
        answer.append(text)

    return answer

"""
n = 5 / arr1 = [9, 20, 28, 18, 11] / arr2 = [30, 1, 21, 17, 28]
return = ["#####", "# # #", "### #", "#  ##", "#####"]

n = 6 / arr1 = [46, 33, 33, 22, 31, 50] / arr2 = [27, 56, 19, 14, 14, 10]
return = ["######", "###  #", "##  ##", " #### ", " #####", "### # "]
"""