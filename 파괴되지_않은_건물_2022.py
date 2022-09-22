"""
N x M 크기의 행렬 모양의 게임 맵이 있습니다. 이 맵에는 내구도를 가진 건물이 각 칸마다 하나씩 있습니다. 적은 이 건물들을 공격하여 파괴하려고 합니다. 건물은 적의 공격을 받으면 내구도가 감소하고 내구도가 0이하가 되면 파괴됩니다. 반대로, 아군은 회복 스킬을 사용하여 건물들의 내구도를 높이려고 합니다.

적의 공격과 아군의 회복 스킬은 항상 직사각형 모양입니다.
예를 들어, 아래 사진은 크기가 4 x 5인 맵에 내구도가 5인 건물들이 있는 상태입니다.

첫 번째로 적이 맵의 (0,0)부터 (3,4)까지 공격하여 4만큼 건물의 내구도를 낮추면 아래와 같은 상태가 됩니다.

두 번째로 적이 맵의 (2,0)부터 (2,3)까지 공격하여 2만큼 건물의 내구도를 낮추면 아래와 같이 4개의 건물이 파괴되는 상태가 됩니다.

세 번째로 아군이 맵의 (1,0)부터 (3,1)까지 회복하여 2만큼 건물의 내구도를 높이면 아래와 같이 2개의 건물이 파괴되었다가 복구되고 2개의 건물만 파괴되어있는 상태가 됩니다.

마지막으로 적이 맵의 (0,1)부터 (3,3)까지 공격하여 1만큼 건물의 내구도를 낮추면 아래와 같이 8개의 건물이 더 파괴되어 총 10개의 건물이 파괴된 상태가 됩니다. (내구도가 0 이하가 된 이미 파괴된 건물도, 공격을 받으면 계속해서 내구도가 하락하는 것에 유의해주세요.)

최종적으로 총 10개의 건물이 파괴되지 않았습니다.

건물의 내구도를 나타내는 2차원 정수 배열 board와 적의 공격 혹은 아군의 회복 스킬을 나타내는 2차원 정수 배열 skill이 매개변수로 주어집니다. 적의 공격 혹은 아군의 회복 스킬이 모두 끝난 뒤 파괴되지 않은 건물의 개수를 return하는 solution함수를 완성해 주세요.
"""


# 건물 내구도 0이하 되면 파괴(아군 회복 스킬로 내구도 회복)
# 계속 공격 받으면 내구도가 0 이하로 떨어질 수 있음
# board -> 건물의 내구도 / 아군의 회복스킬 또는 적의 공격을 나타내는 2차원 정수 배열 skill
# 모두 끝난 뒤 파괴되지 않은 건물의 개수를 return
# skill 열의 길이 6 [type, r1, c1, r2, c2, degree]
# type는 1 혹은 2 1(공격) 2(회복)
# import copy


def solution(board, skill):
    answer = 0
    dead_num = 0
    # board의 크기 받기
    col = len(board[0])
    row = len(board)
    second_board = [[0] * (col + 1) for i in range(row + 1)]
    dead_num = 0
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = - degree
        second_board[r1][c1] = second_board[r1][c1] + degree
        second_board[r1][c2 + 1] = second_board[r1][c2 + 1] - degree
        second_board[r2 + 1][c1] = second_board[r2 + 1][c1] - degree
        second_board[r2 + 1][c2 + 1] = second_board[r2 + 1][c2 + 1] + degree

    # print(second_board)
    for i in range(row):
        for j in range(col):
            second_board[i][j + 1] = second_board[i][j] + second_board[i][j + 1]

    for i in range(row):
        for j in range(col):
            second_board[i + 1][j] = second_board[i + 1][j] + second_board[i][j]

    for i in range(row):
        for j in range(col):
            board[i][j] = board[i][j] + second_board[i][j]
            if board[i][j] <= 0:
                dead_num = dead_num + 1
    # print(board)
    answer = col * row - dead_num
    return answer

"""
board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
return = 10

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
skill = [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]
return = 6
"""