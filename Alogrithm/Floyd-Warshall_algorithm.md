# Floyd-Worshall Algorithm
> 모든 노드 간 최단 경로를 구하는 문제

## idea
A 에서 다른 노드 B 로 가는 비용은 다른 노드를 경로로 삼고 가거나 바로 가는 경우 2 가지 뿐이다.  

```
for k in range(n+1):
    for row in range(n+1):
        for col in range(n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] dist[k][j])
```

## Reference
[Reference](https://chanhuiseok.github.io/posts/algo-50/)