# binary_search

## 정렬된 상태에서 해야 함
```
while start <= end:
    mid = (start + end) // 2
    
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
```

## 증명
invariant : 만약 어떤 i 에 대해서 a[i] == target 이면 left<=i<=right가 항상 성립한다.  

a[i] == target인 i가 없다면 루프는 언젠간 반드시 끝나고 -1을 리턴, i가 있다면 루프 안에서 반드시 리턴 됨
