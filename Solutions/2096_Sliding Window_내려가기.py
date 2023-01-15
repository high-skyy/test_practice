

import sys
N = int(sys.stdin.readline())
DP = [[{'min_val' : 0, 'max_val' : 0} for i in range(3)] for _ in range(2)]
board = list(map(int, sys.stdin.readline().split(' ')))
for i in range(3):
    DP[0][i]['min_val'] = board[i]
    DP[0][i]['max_val'] = board[i]
if N == 1:
    print(max(DP[0][0]['max_val'], DP[0][1]['max_val'], DP[0][2]['max_val']),
          min(DP[0][0]['min_val'], DP[0][1]['min_val'], DP[0][2]['min_val']))
else:
    board = list(map(int, sys.stdin.readline().split(' ')))
    DP[1][0]['min_val'] = min(DP[0][0]['min_val'], DP[0][1]['min_val']) + board[0]
    DP[1][0]['max_val'] = max(DP[0][0]['max_val'], DP[0][1]['max_val']) + board[0]
    DP[1][1]['min_val'] = min(DP[0][0]['min_val'], DP[0][1]['min_val'], DP[0][2]['min_val']) + board[1]
    DP[1][1]['max_val'] = max(DP[0][0]['max_val'], DP[0][1]['max_val'], DP[0][2]['max_val']) + board[1]
    DP[1][2]['min_val'] = min(DP[0][1]['min_val'], DP[0][2]['min_val']) + board[2]
    DP[1][2]['max_val'] = max(DP[0][1]['max_val'], DP[0][2]['max_val']) + board[2]
    for _ in range(N-2):
        for i in range(3):
            DP[0][i]['min_val'] = DP[1][i]['min_val']
            DP[0][i]['max_val'] = DP[1][i]['max_val']
        board = list(map(int, sys.stdin.readline().split(' ')))
        DP[1][0]['min_val'] = min(DP[0][0]['min_val'] , DP[0][1]['min_val']) + board[0]
        DP[1][0]['max_val'] = max(DP[0][0]['max_val'] , DP[0][1]['max_val']) + board[0]
        DP[1][1]['min_val'] = min(DP[0][0]['min_val'] , DP[0][1]['min_val'], DP[0][2]['min_val']) + board[1]
        DP[1][1]['max_val'] = max(DP[0][0]['max_val'] , DP[0][1]['max_val'], DP[0][2]['max_val']) + board[1]
        DP[1][2]['min_val'] = min(DP[0][1]['min_val'] , DP[0][2]['min_val']) + board[2]
        DP[1][2]['max_val'] = max(DP[0][1]['max_val'] , DP[0][2]['max_val']) + board[2]
    print(max(DP[1][0]['max_val'], DP[1][1]['max_val'], DP[1][2]['max_val']),
          min(DP[1][0]['min_val'], DP[1][1]['min_val'], DP[1][2]['min_val']))

