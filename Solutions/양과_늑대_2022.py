def solution(info, edges):
    answer = 0
    global max_sheep
    max_sheep = 0
    visited = [0]
    sheep_num = 1
    wolf_num = 0
    dfs(visited, sheep_num, wolf_num, edges, info)
    answer = max_sheep
    return answer


def dfs(visited, sheep_num, wolf_num, edges, info):
    global max_sheep
    # 종료 조건
    if sheep_num <= wolf_num:
        return
    else:
        if sheep_num > max_sheep:
            # print("here")
            print(sheep_num)
            max_sheep = sheep_num

    # iteration
    for every_node in visited:
        children = find_children(every_node, edges)
        if children:
            for every_child in children:
                if every_child not in visited:
                    new_visited = visited[:]
                    new_visited.append(every_child)
                    if info[every_child] == 0:
                        dfs(new_visited, sheep_num + 1, wolf_num, edges, info)
                    else:
                        dfs(new_visited, sheep_num, wolf_num + 1, edges, info)
                else:
                    continue
        else:
            continue


def find_children(node, edges):
    children = []
    for every_edge in edges:
        if every_edge[0] == node:
            children.append(every_edge[1])
    return children

"""
info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
return = 5

info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
return = 5
"""