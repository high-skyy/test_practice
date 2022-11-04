# 알고력과 코딩력은 0이상의 정수
# 공부 (1의 시간당 1씩 올라가고) or 문제풀기로 올림
# 문제가 요구하는 시간 필요 + 같은 문제를 여러 번 푸는 것이 가능하다.
# problems = [[10,15,2,1,2],[20,20,3,3,4]]
# 모든 문제들을 풀 수 있는 알고력과 코딩력
import heapq


def solution(alp, cop, problems):
    answer = 0
    max_alp, max_cop = [-1, -1]

    # [alp_req, cop_req, alp_rwd, cop_rwd, cost]
    for problem in problems:
        max_alp = problem[0] if problem[0] > max_alp else max_alp
        if problem[1] > max_cop:
            max_cop = problem[1]

    max_cop = max(max_cop, cop)
    max_alp = max(max_alp, alp)

    memory = [[100 * (150 + 150) + 1 for i in range(0, max_cop + 1)] for j in range(0, max_alp + 1)]
    memory[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                memory[i + 1][j] = min(memory[i][j] + 1, memory[i + 1][j])
            if j + 1 <= max_cop:
                memory[i][j + 1] = min(memory[i][j] + 1, memory[i][j + 1])
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    memory[min(i + alp_rwd, max_alp)][min(j + cop_rwd, max_cop)] = min(
                        memory[min(i + alp_rwd, max_alp)][min(j + cop_rwd, max_cop)], memory[i][j] + cost)

    return memory[max_alp][max_cop]