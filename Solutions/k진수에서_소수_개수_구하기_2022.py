"""
양의 정수 n이 주어집니다. 이 숫자를 k진수로 바꿨을 때,
변환된 수 안에 아래 조건에 맞는 소수(Prime number)가 몇 개인지 알아보려 합니다.

0P0처럼 소수 양쪽에 0이 있는 경우
P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
P처럼 소수 양쪽에 아무것도 없는 경우
단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
예를 들어, 101은 P가 될 수 없습니다.
예를 들어, 437674을 3진수로 바꾸면 211020101011입니다. 여기서 찾을 수 있는 조건에 맞는 소수는 왼쪽부터 순서대로 211, 2, 11이 있으며, 총 3개입니다. (211, 2, 11을 k진법으로 보았을 때가 아닌, 10진법으로 보았을 때 소수여야 한다는 점에 주의합니다.) 211은 P0 형태에서 찾을 수 있으며, 2는 0P0에서, 11은 0P에서 찾을 수 있습니다.

정수 n과 k가 매개변수로 주어집니다. n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 위 조건에 맞는 소수의 개수를 return 하도록 solution 함수를 완성해 주세요.
1 ≤ n ≤ 1,000,000
3 ≤ k ≤ 10
"""


def check_prime(n):
    # 1 또는 2인 경우
    if n == 1:
        return False
    elif n == 2:
        return True
    # 2 이상인 경우
    find_root = 2
    while n > find_root * find_root:
        find_root = find_root + 1
    for i in range(find_root + 1):
        if i >= 2:
            if n % i == 0:
                return False
    return True


def change_format(n, k):
    format = ''
    l = k
    # 가장 높은 자릿수
    while n >= k:
        k = k * l
    k = k / l
    while n > 0:
        if n >= k:
            left_over = int(n / k)
            n = n - k * left_over
            k = int(k / l)
            format = format + str(left_over)
        else:
            k = int(k / l)
            format = format + str(0)
    return format


def solution(n, k):
    answer = 0
    blank = ''
    format = change_format(n, k)
    list_to_check = []
    list_to_check = list(format.split('0'))
    print(" k is : ", k)
    if len(list_to_check) == 0:
        return 0
    while blank in list_to_check:
        list_to_check.remove(blank)
    list_to_check = list(map(int, list_to_check))
    print("list_to_check : ", list_to_check)
    answer_list = []
    for every_element in list_to_check:
        answer_list.append(every_element)
    print("answer_list : ", answer_list)
    for every_number in answer_list:
        if check_prime(every_number) == True:
            answer = answer + 1

    return answer

"""
n = 437674 / k = 3 / return 3
n = 110011 / k = 10 / return 2
"""