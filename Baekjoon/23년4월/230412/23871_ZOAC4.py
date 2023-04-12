import sys

H, W, N, M = map(int, sys.stdin.readline().split())
room = [[0] * W for _ in range(H)]
print(room)