# 2차원 가상 벽면에 기둥과 보를 이용한 구조물을 설치할 수 있는데, 기둥과 보는 길이가 1인 선분
# 기둥은 바닥 위 보의 한쪽 끝 부분 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나 양쪽 끝 부분이 다른 보와 동시에 연결
# 작업을 수행한 결과가 조건을 만족하지 않는다면 해당 작업은 무시됩니다.
# [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]] -> build_frame (가로 : 4, 세로 1~1000)
# [x,y,a,b] x,y 교차점(오른쪽 위쪽 기준) a -> 0 : (기중) 1 : 보, b : 0 삭제 1: 설치
# return 하는 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
# x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.

def solution(n, build_frame):
    answer = []
    # 기둥 : 0, 보 : 1 / 삭제 : 0 설치 : 1
    for inst in build_frame:
        if inst[3] == 1:  # 설치
            answer.append([inst[0], inst[1], inst[2]])
            if not check(answer):
                answer.remove([inst[0], inst[1], inst[2]])
        else:
            answer.remove([inst[0], inst[1], inst[2]])
            if not check(answer):
                answer.append([inst[0], inst[1], inst[2]])
    if not answer:
        return [[]]
    return sorted(answer)


def check(answer):
    result = True
    # 기둥 : 0, 보 : 1
    for x, y, struct in answer:
        if struct:  # 보
            # 보는 한쪽 끝 부분이 기둥 위에 있거나 양쪽 끝 부분이 다른 보와 동시에 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
        else:  # 기둥
            # 기둥은 바닥 위 보의 한쪽 끝 부분 또는 다른 기둥 위에 있어야 합니다.
            if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                continue
            else:
                return False
    return result

solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]])
"""
n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
"""