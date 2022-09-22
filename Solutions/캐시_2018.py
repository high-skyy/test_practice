# chacheSize = 3  / 정수 0부터 30 사이이다.
# cities = "Jeju", "Pangyo", "Seoul", "NewYork", "LA", 최대 100,000개
# 영문자, 대소문자 구분 x

from collections import deque


def solution(cacheSize, cities):
    answer = 0
    # hit : 1, miss : 5

    q = deque()
    time = 0
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        city = city.lower()
        if city not in q:
            time += 5
            if len(q) == cacheSize:
                q.popleft()
                q.append(city)
            else:
                q.append(city)
        else:
            time += 1
            for i in range(len(q)):
                if q[i] == city:
                    q.remove(city)
                    q.append(city)
    answer = time

    return answer

"""
cacheSize = 3 / cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
return = 50

cacheSize = 3 / cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
return = 21
"""