# 양방향 쉼터 / 산봉우리 휴식 / intensity (path 중 두 노드 사이의 최댓값)
# 한번만 가는 것 까지 계산

from collections import defaultdict
import heapq


def solution(n, paths, gates, summits):
    answer = 0
    INF = float('inf')
    min_list = [INF, -1]
    # n : 산의 지점 수, paths : 등산로 [i, j, w], gates : 출입구, summits : 산봉우리
    path_dict = defaultdict(list)
    for i, j, w in paths:
        path_dict[i].append([j, w])
        path_dict[j].append([i, w])
    # print(path_dict)
    for gate in gates:
        q = [(0, gate)]  # intensity, cur
        intensity_list = [[INF, i] for i in range(n + 1)]
        min_intensity = INF
        while q:
            print(q)
            intensity, cur = heapq.heappop(q)
            if cur in summits:
                min_intensity = min(min_intensity, intensity)
            if intensity > min_intensity:
                break
            if intensity_list[cur][0] < intensity:
                continue
            for end, distance in path_dict[cur]:
                heapq.heappush(q, (max(intensity, distance), end))
                intensity_list[end][0] = min(intensity_list[end][0], distance)
        intensity_list = sorted(intensity_list)
        candidate = intensity_list[0]
        if candidate[0] < min_list[0]:
            min_list = [candidate[0], candidate[1]]
        elif candidate[0] == min_list[0]:
            if candidate[1] < min_list[1]:
                min_list = [candidate[0], candidate[1]]
        else:
            continue

    answer = min_list
    return answer


solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3], [5])