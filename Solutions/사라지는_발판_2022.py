# board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# aloc, bloc = [1,0]


def solution(board, aloc, bloc):
    answer = -1
    global d_row, d_col
    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]
    del_loc = []
    answer = dfs(board, aloc, bloc, "A", del_loc, 0)[1]

    return answer


def dfs(board, aloc, bloc, mode, del_loc, depth):
    global d_row, d_col
    if mode == "A":
        child_results = []
        A_win = []
        B_win = []
        for i in range(4):
            row = aloc[0] + d_row[i]
            col = aloc[1] + d_col[i]
            if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]):
                if board[row][col] == 1:
                    if [row, col] not in del_loc:
                        new_del_loc = del_loc[:]
                        new_del_loc.append(aloc)
                        child_results.append(dfs(board, [row, col], bloc, "B", new_del_loc, depth + 1))
        if child_results:
            if aloc == bloc:
                return ["A_win", depth + 1]
            for every_result in child_results:
                if every_result[0] == "A_win":
                    A_win.append(every_result[1])
                else:
                    B_win.append(every_result[1])
            if A_win:
                return ["A_win", min(A_win)]
            else:
                return ["B_win", max(B_win)]
        else:
            return ["B_win", depth]
    else:
        child_results = []
        A_win = []
        B_win = []
        for i in range(4):
            row = bloc[0] + d_row[i]
            col = bloc[1] + d_col[i]
            if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]):
                if board[row][col] == 1:
                    if [row, col] not in del_loc:
                        new_del_loc = del_loc[:]
                        new_del_loc.append(bloc)
                        child_results.append(dfs(board, aloc, [row, col], "A", new_del_loc, depth + 1))
        if child_results:
            if aloc == bloc:
                return ["B_win", depth + 1]
            for every_result in child_results:
                if every_result[0] == "A_win":
                    A_win.append(every_result[1])
                else:
                    B_win.append(every_result[1])
            if B_win:
                return ["B_win", min(B_win)]
            else:
                return ["A_win", max(A_win)]
        else:
            return ["A_win", depth]

"""
board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]
return = 5

board = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]
return = 4

board = [[1, 1, 1, 1, 1]]
aloc = [0, 0]
bloc = [0, 4]
return = 4

board = [[1]]
aloc = [0, 0]
bloc = [0, 0]
return = 0

"""