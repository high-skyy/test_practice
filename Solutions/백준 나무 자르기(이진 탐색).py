# 적어도 M미터 가져가야 함 높이 최댓 값
#

N, M = map(int, input().split(' '))
length_list = list(map(int, input().split(' ')))

end = max(length_list)
start = 1
max_possible = 0

def sumcut(mid):
    total_length = 0
    for length in length_list:
        if length < mid:
            continue
        else:
            total_length += length - mid
    return total_length

while start <= end:
    mid = (start + end) // 2
    total_length = sumcut(mid)
    if total_length >= M:
        max_possible = max(max_possible, mid)
        start = mid + 1
    else:
        end = mid - 1
print(max_possible)
