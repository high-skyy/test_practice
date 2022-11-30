# 코딩 테스트 준비

## 행동강령
1. 문제 천천히 읽어도 괜찮다. 꼼꼼하게 다 확인하자.
2. 아이디어는 문제에 직접 예시까지 확인하자.
3. 필요한 조건은 적어주자.

## 데이터 크기 제한 & 시간 복잡도
- n <= 1,000,000        :       O(n) or O(n*log(n))
- n <= 10,000           :             O(n**2)
- n <= 500              :             O(n**3)
100000000
```
1. list 뒤집기
list[::-1]
del list1[index], list1.pop(index)
list1.remove(value)
list1.insert(index, object)
list1.count(value)

2. sort
list1.sort()
list1 = (list1, reverse = True/False key = lambda x : x[1])

3. regular expression (import re)               /       [a-z]
re.findall( "(찾고 싶은 문자열)", 찾음을 당하는 문자열)

4. re.sub("패턴", "대체 할 패턴", 해당 문자열)

5. c = lambda t : c = lambda t : int(t[0:2])*3600 + int(t[3:5])*60 + int(t[6:8])

6. f"(문자열){(변수):(0공백)(화살표)(자릿수)}    # 공백을 0으로 채운다 / 소수 자릿수 지정 자릿수 다음에 '.' + (소수 몇 째 자리) + f
answer = f"{hour:2}:{minutes:2}:{second:2}"

7. dq.rotate
```

## IDEA
1. 1차원 or 2차원 배열 변환
  - list 2개 이어 붙히기 + 확장 (두 큐 합 같게 만들기)
2. 경우의 수가 적은 경우에는 다 만들생각
  - 성격 유형 검사하기, 숫자 문자열과 영단어(one4seveneight)
3. 디엑스트라 algorithm heap으로 구현 (visited 잊지 말자)
  - 등산 코스 정하기, 합승 택시 요금
4. DP (dp[i][j] -> 점화식 처럼)
  - 코딩 테스트 공부
5. linked-list (node 구현 : 원래 자리 / deque로 구현 뜯어서 붙일 때)
  - 행렬과 연산
6. BFS
  - 거리두기 확인하기
7. 더블 pointer or window
  - 보석 쇼핑
8. 구간에 대한 누적합
  - 파괴되지 않는 건물,
9. alpha-beta tree
  - 사라지는 발판
10. 완전 탐색
  - 양과 늑대
14. 구간합 : 미리 구해서 한칸 씩
15. 일반화 : 원형을 일직선으로
16. window : 구간을 정해서 앞으로 가면서 더하거나 빼기
  - 광고 삽입


## 재귀로 풀 경우 깊이 때문에 런타임 에러가 발생할 수 있음
> 아래와 같은 코드로 이를 해결할 수 있다.
```
import sys
sys.setrecursionlimit(10**6)
```

