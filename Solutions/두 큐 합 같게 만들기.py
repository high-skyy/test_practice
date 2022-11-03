# 길이가 같은 큐 2개 한번의 pop(큐의 맨 앞)과 한번의 insert(배열 끝)를 합쳐서 작업 1회
# 길이가 300,000 -> n^2 간당간당

from collections import deque


def solution(queue1, queue2):
    answer = -1

    total_sum = sum(queue1) + sum(queue2)
    if total_sum % 2 == 1:
        return answer
    else:
        half = int(total_sum / 2)

    extended_queue = queue1 + queue2 + queue1 + queue2
    length = len(extended_queue)
    start = 0
    end = len(queue1) - 1
    current_sum = sum(queue1)
    count = 0
    while True:
        if current_sum == half:
            return count
        elif current_sum < half:
            end += 1
            if end == length:
                return -1
            else:
                count += 1
            current_sum += extended_queue[end]
        else:
            start += 1
            current_sum -= extended_queue[start - 1]
            count += 1

    return answer