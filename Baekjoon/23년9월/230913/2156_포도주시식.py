import sys

input = sys.stdin.readline

N = int(input().strip())
wine = [int(input().strip()) for _ in range(N)]

# 마실 수 있는 최대 포도주 양을 저장해 줄 dp
dp = [0] * N
dp[0] = wine[0]
if N > 1:
    dp[1] = wine[0] + wine[1]
if N > 2:
    dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])
if N > 3:
    # 연속으로 놓여진 3잔을 모두 마실 수는 없음
    # 현재 포도주 O, 이전 포도주 O, 전전 포도주 X
    # 현재 포도주 O, 이전 포도주 X, 전전 포도주 O
    # 현재 포도주 X
    for i in range(3, N):
        dp[i] = max(wine[i] + wine[i - 1] + dp[i - 3], wine[i] + dp[i - 2], dp[i - 1])

print(dp[N - 1])