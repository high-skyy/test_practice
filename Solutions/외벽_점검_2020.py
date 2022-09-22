# 취약 지점 점검시간 1시간
# 외벽의 길이 n
# 취약 지점 -> weak = [1, 5, 6, 10]
# 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 -> dist = 	[1, 2, 3, 4]
# answer = 보내야 하는 친구의 수의 최소 값 (안되는 경우 : -1)

from itertools import permutations


def solution(n, weak, dist):
    answer = 0
    length = len(weak)
    weak = weak + [n + weak[i] for i in range(length)]
    # print(weak) [1, 5, 6, 10, 13, 17, 18, 22]
    global min_value
    min_value = len(dist) + 1

    for i in range(0, length):
        check = weak[i:i + length]
        for perm in permutations(dist, len(dist)):
            # print("perm is : ", perm)
            cur_loc = check[0]
            dist_list = list(perm)
            count = 0
            while dist_list:
                count += 1
                distance = dist_list.pop()
                next_loc = cur_loc + distance
                for i in range(length):
                    if check[i] <= next_loc:
                        continue
                    else:
                        cur_loc = check[i]
                        break
                if next_loc >= check[len(check) - 1]:
                    if count < min_value:
                        min_value = count
                    break

    answer = min_value
    if answer == len(dist) + 1:
        return -1
    return answer
"""
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
"""
"""
원형을 직선화해서 일반화 시킨다.
"""