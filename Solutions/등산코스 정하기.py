# 알고력과 코딩력은 0이상의 정수
# 공부 (1의 시간당 1씩 올라가고) or 문제풀기로 올림
# 문제가 요구하는 시간 필요 + 같은 문제를 여러 번 푸는 것이 가능하다.
# problems = [[10,15,2,1,2],[20,20,3,3,4]]
# 모든 문제들을 풀 수 있는 알고력과 코딩력
import heapq


def solution(alp, cop, problems):
    answer = 0

    max_alp, max_cop = [-1, -1]

    for problem in problems:
        if problem[0] > max_alp:
            max_alp = problem[0]
        if problem[1] > max_cop:
            max_cop = problem[0]
    print(max_alp, max_cop)
    memory = [[100 * max(max_alp, max_cop) for i in range(0, max_alp + 1)] for j in range(0, max_cop + 1)]
    memory[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i == alp and j == cop:
                continue
            else:
                # 공부
                if i == 0:
                    memory[i][j] = min(memory[i][j], memory[i][j - 1] + 1)
                if j == 0:
                    print("i is : ", i)
                    print("j is : ", j)
                    print(memory[i-1][j])
                    print(memory[i][j])
                    memory[i][j] = min(memory[i - 1][j] + 1, memory[i][j])
                if i != 0 and j != 0:
                    memory[i][j] = min(memory[i][j], memory[i - 1][j] + 1, memory[i][j - 1] + 1)
                # 문제 해결
                #  [alp_req, cop_req, alp_rwd, cop_rwd, cost]
                for problem in problems:
                    if i - problem[2] < problem[0] or j - problem[3] < problem[1] or i - problem[2] < alp or j - \
                            problem[2] < cop:
                        continue
                    else:
                        memory[i][j] = min(memory[i][j], memory[i - problem[2]][j - problem[3]] + problem[4])
    print(memory[max_alp][max_cop])
    return memory[max_alp][max_cop]

solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]])