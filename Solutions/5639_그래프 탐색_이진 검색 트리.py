# 전위 순위 (VLR) -> (LRV) 구하기
'''
주의
1. 같은 키를 가지는 노드는 없다.
2. output : 후위 순위 한 결과를 한줄에! 하나씩! 출력한다.
'''

import sys
node_list = []
while True:
    cur = sys.stdin.readline()
    print("here")
    if cur == '\n':
        break
    else:
        node_list.append(int(cur))
print(node_list)