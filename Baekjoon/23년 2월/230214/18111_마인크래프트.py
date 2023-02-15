import sys

N, M, B = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max, min = 0, 256
for i in range(N):
    for j in range(M):
        if board[i][j] > max:
            max = board[i][j]
        elif board[i][j] < min:
            min = board[i][j]
print(max, min)