# 코딩 테스트 준비

## 행동강령
1. 문제 천천히 읽어도 괜찮다. 꼼꼼하게 다 확인하자.
2. 문제를 따라가도 좋지만 간단하게 생각하자. (for문 많이 돌려도 됨)

## IDEA
1. Transformation : (주차 요금 계산 2022)
2. 완전 탐색 : (양과 늑대 2022)
3. alpha-beta tree : (사라지는 발판 2022) / 결과가 나오는 것 부터 비교
4. 다익스트라 algo : 합승 택시 요금
5. 누적합 : 파괴되지 않은 건물
6. 구간합 : 미리 구해서 한칸 씩
7. 일반화 : 원형을 일직선으로
8. window : 구간을 정해서 앞으로 가면서 더하거나 빼기

## 최근 체화 함수
1. list_slicing, (string에도 적용 가능)  
```
list[start:end:step]
# 음수가 가능하다. 맨 마지막 원소 -1 기준 왼쪽으로 1씩 작아짐
```
2. Sorted 함수
syntax : 리스트명.sort( )
```
# 원래 list 자체가 변형된다.
```
syntax : sorted ( 리스트명, reverse = True/False, key = 해당 파라미터 )
```
list2 = [[1,2], [2,1], [1,3], [3,1]]
print(sorted(list2, key = lambda x : x[1]))   # [[2, 1], [3, 1], [1, 2], [1, 3]]
```

3. [[0] * 5] [[0,0,0,0,0]]

4. re.findall( "(찾고싶은 문자열)", 찾음을 당하는 문자열 )  
> ex) ([a-z])

5. re.sub( "패턴", "대체 할 패턴", 해당 문자열 )
> 새롭게 반환해서 받아 주어야 함

6. dict도 sorted 사용 가능 삽입한 원소 순서대로 저장됨
```
operator.itemgetter(1)
https://blockdmask.tistory.com/566#:~:text=1.%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC%20key%20%EC%A0%95%EB%A0%AC&text=sorted%20%ED%95%A8%EC%88%98%EB%8A%94%20%EC%A0%95%EB%A0%AC%ED%95%A0,%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC%EB%A1%9C%20%EB%B3%80%ED%99%98%ED%95%B4%EC%A3%BC%EB%A9%B4%20%EB%90%A9%EB%8B%88%EB%8B%A4.
```

7. labmda 이용
```
c = lambda t : int(t[0:2])*3600 + int(t[3:5])*60 + int(t[6:8])
```


## 재귀로 풀 경우 깊이 때문에 런타임 에러가 발생할 수 있음
> 아래와 같은 코드로 이를 해결할 수 있다.
```
import sys
sys.setrecursionlimit(10**6)
```

## 데이터 크기 제한 & 시간 복잡도
- n <= 1,000,000        :       O(n) or O(n*log(n))
- n <= 10,000           :             O(n**2)
- n <= 500              :             O(n**3)
