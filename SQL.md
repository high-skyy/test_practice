# SQL

## TIP
겹치는 것이 없으면 굳이 I.뭐를 쓸 필요가 없음.

## 기본
- SELECT 절은 , 로
- FROM 절도 , 로
- WHERE 절의 경우는 AND 로
- GROUP BY 의 경우 , 로
- ORDER BY 의 경우 , 로

## 이중 order by
결과 집합을 여러 열로 정렬하려면 ORDER BY 절에 ,(쉼표) 로 구분된 열 목록을 지정합니다.

```
SELECT * FROM 테이블 ORDER BY STATUS DESC, CREATED_AT;
```
> 먼저 결과 집합을 'status'값을 기준으로 내림차순으로 정렬합니다. 그런 다음 정렬 된 결과 집합을
> status 값이 같은 경우 'createdAt' 값을 기준으로 오름차순으로 정렬합니다.

- [Reference](https://dar0m.tistory.com/60)

## 함수 종류

### DATE_FORMAT 함수
이 함수는 DATETIME의 TYPE을 가진 칼럼의 형식을 수정, 지정해 주는 함수이다.
- date의 type을 가진 값도 like가 사용이 가능하다.
```
DATE_FORMAT("날짜값, 날짜칼럼", "%Y");
```
뒤에 "%Y" 등은 형식을 지정해준다.
ex) %Y/%M/%D
- Format Description
  - %Y : 연도를 4자리로
  - %y : 연도를 2자리로
  - %M : 달 이름을 Full Name으로 (March)
  - %m : 달 이름을 00 ~ 12 숫자로
  - %D : 일 이름을 1st... 등으로
  - %d : 일 이름을 숫자로 

### COUNT
테이블에 존재하는 데이터 갯수를 가져오고 싶을 때가 있습니다.
이때 사용하는 함수가 COUNT 함수입니다.
COUNT 함수는 테이블에 컬럼의 데이터 갯수를 가져옵니다.
- 주의 : 이때 NULL인 데이터는 제외하고 계산합니다.
- 전체 행 갯수를 가져올 때는 컬럼 대신에 *를 지정합니다.

### ROUND

### HOUR

### MONTH

## Inner join 과 natural join의 차이
- Inner join
  - default join
  - join 조건에서 동일한 값이 있는 행 만을 반환한다.
  - 반드시 ON 절을 써주어야 한다.
- Natural join
  - join 조건에서 동일한 이름을 갖는 모든 칼럼들에 대해 equi join이 수행됨
  - join이 되는 테이블의 데이터 도메인과 칼럼명 칼럼값이 동일해야 하는 제약 조건이 있다.

## 명시적 조인 표현
```
SELECT *
FROM EMPLOYEE INNER JOIN DEPARTMENT
ON EMPLOYEE.DEPARTMENTID = DEPARTMENT.DEPARTMENTID;
```
## 암시적 조인 표현
```
SELECT *
FROM EMPLOYEE E, DEPARTMENT D
WHERE E.DEPARTMENTID = DEPARTMENT.DEPARTMENTID;
```

## like
```
SELECT * FROM TABLE_NAME
WHERE TABLE_NAME.ATTRIBUTE
LIKE '스타%';
```
- 'a%' : a로 시작하는 문자 찾기
- '%a' : a로 끝나는 문자열 조회
- '%a%' : a문자가 포함된 값 모두 조회
- '음_' : 음으로 시작하는 글자가 두 개인 문자열 조회
- : 같은 경우에는 글자 수를 정해준다.

## UNION ALL
말 그대로 합집합 (aliasing이 필요가 없다)

## NULL
null 넣고 싶으면 select 부분에 null as column명으로 넣을 수 있다.

## BETWEEN
특정 값의 범위를 
```
SELECT *
FROM [테이블 명]
WHERE [컬럼명] BETWEEN 값1 AND 값2
```

## IN
명시된 데이터들에 해당 정보가 있을 때
```
SELECT USERID, NAME, ADDR
FROM USERTBL
WHERE ADDR IN ('경남', '전남', '경북', '전북')
```

## Reference
- [Reference](https://jhnyang.tistory.com/420)
- [Reference](https://extbrain.tistory.com/54)