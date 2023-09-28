import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input().strip()) for _ in range(n)]
# dp[i] : 합이 i원이 되는 경우의 수
dp = [0] * (k + 1)
dp[0] = 1   # 동전을 한개만 쓸 때

for i in coin:
    for j in range(i, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[k])