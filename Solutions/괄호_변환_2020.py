# p = "(()())()"  // result = "(()())()"

def solution(p):
    answer = ''
    # 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not p:
        return p
    else:
        if divide(p):
            u, v = divide(p)
            if check(u):
                answer = u + solution(v)
                print(answer)
                return answer
            else:
                temp = "("
                temp += solution(v)
                temp += ")"
                u_1 = u[1:len(u) - 1]
                u_2 = ""
                for i in u_1:
                    if i == "(":
                        u_2 += ")"
                    else:
                        u_2 += "("
                print(temp + u_2)
                return temp + u_2
    # 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    print(answer)
    return answer


def check(p):
    left, right = 0, 0
    for i in p:
        if i == "(":
            left += 1
        else:
            right += 1
        if left - right < 0:
            return False
    return True


def divide(p):
    u, v = "", ""
    left, right = 0, 0
    for i in p:
        if i == "(":
            left += 1
        else:
            right += 1
        u += i
        if left == right:
            return [u, p[len(u):]]
    return []
solution("(()())()")
"""
test - case
p = "(()())()" return = "(()())()"
p = ")("        return = "()"
p = "()))((()"  return = "()(())()"
"""