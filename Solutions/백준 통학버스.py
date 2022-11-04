import heapq

number_of_houses, bus_max_people, school_location = map(int, input().split(' '))
answer = 0
left = []
right = []
for _ in range(number_of_houses):
    house_location, people_living = map(int, input().split(' '))
    if house_location > school_location:
        heapq.heappush(right, tuple([school_location - house_location, people_living]))
    elif house_location < school_location:
        heapq.heappush(left, tuple([house_location - school_location, people_living]))

people_on_bus = 0
max_distance = 0
while left:
    dist, people_living = heapq.heappop(left)
    dist = -dist
    max_distance = max(max_distance, dist)
    if people_on_bus + people_living > bus_max_people:
        answer += max_distance * 2
        heapq.heappush(left, tuple([-dist, people_living - bus_max_people + people_on_bus]))
        people_on_bus = 0
        max_distance = 0
    else:
        people_on_bus += people_living
if max_distance != 0:
    answer += max_distance*2
    max_distance = 0
    people_on_bus = 0
# print(answer)

while right:
    dist, people_living = heapq.heappop(right)
    dist = -dist
    max_distance = max(max_distance, dist)
    if people_on_bus + people_living > bus_max_people:
        answer += max_distance * 2
        heapq.heappush(right, tuple([-dist, people_living - bus_max_people + people_on_bus]))
        people_on_bus = 0
        max_distance = 0
    else:
        people_on_bus += people_living
if max_distance != 0:
    answer += max_distance * 2
print(answer)


"""
학교 -> 하나 (학교에서 버스 시작)
각 아파트 단지마다 학생 수

3 4 4
0 1
2 2
5 1
"""