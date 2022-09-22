# Dijkstra algorithm
> 어떠한 노드로부터 나머지 노드로 가는 최단 경로의 수 구하는 알고리즘

## 순서
1. 출발 노드 선정
2. 출발 노드 기준으로 각 노드의 최소 비용 저장
3. 방문하지 않은 노드 중 가장 비용이 적은 노드 선택
4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용을 갱신
5. 위 과정 3~4 반복

## example  
![다익스트라 알고리즘](https://user-images.githubusercontent.com/105041834/191743927-52e40a6e-ff5c-48dc-b3a2-c60acccf676b.JPG)  
[출처](https://m.blog.naver.com/ndb796/221234424646)  

- Implementation은 이차원 배열로 row -> col으로 가는 비용

- initialize
![다익스트라 implementation](https://user-images.githubusercontent.com/105041834/191744408-f3f49fde-4190-4148-bd58-820e56dccab4.JPG)  
[출처](https://m.blog.naver.com/ndb796/221234424646)  

- result
![다익스트라 결과](https://user-images.githubusercontent.com/105041834/191744882-13f046bf-9eef-45f4-a5f6-9b7e779e1d0b.JPG)



## Reference
[Reference](https://m.blog.naver.com/ndb796/221234424646)