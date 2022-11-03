# 길 : 시간 , 단 방향, 함정 가면 연결된 모든 화살표 방향이 바뀐다.
# 1 부터 n개의 방

from collections import defaultdict
import heapq


def solution(n, start, end, roads, traps):
    answer = 0
    reverse = 0

    road_dict = defaultdict(list)
    road_reverse = defaultdict(list)
    for p, q, s in roads:
        road_dict[p].append([q, s])
        road_reverse[q].append([p, s])

    q = []

    visited_traps = [0 for i in range(0, n + 1)]
    visited = []
    visited.append([start] + visited_traps)
    heapq.heappush(q, [0, start, visited_traps])
    while q:
        time, cur, visited_traps = heapq.heappop(q)
        visited.append([cur] + visited_traps)
        if cur == end:
            return time

        for dest, cost in road_dict[cur]:
            if (visited_traps[dest] + visited_traps[cur]) % 2 == 0:
                if dest in traps:
                    new_visited_traps = visited_traps[:]
                    new_visited_traps[dest] = (new_visited_traps[dest] + 1) % 2
                    if ([dest] + new_visited_traps) not in visited:
                        heapq.heappush(q, [time + cost, dest, new_visited_traps])
                else:
                    if ([dest] + visited_traps) not in visited:
                        heapq.heappush(q, [time + cost, dest, visited_traps])

        for dest, cost in road_reverse[cur]:
            if (visited_traps[dest] + visited_traps[cur]) % 2 == 1:
                if dest in traps:
                    new_visited_traps = visited_traps[:]
                    new_visited_traps[dest] = (new_visited_traps[dest] + 1) % 2
                    if ([dest] + new_visited_traps) not in visited:
                        heapq.heappush(q, [time + cost, dest, new_visited_traps])
                else:
                    if ([dest] + new_visited_traps) not in visited:
                        heapq.heappush(q, [time + cost, dest, visited_traps])
    return answer