import sys
input = sys.stdin.readline

N = int(input().strip())
# 빨/초/파로 칠하는 비용 price
price = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]

for i in range(3):
    dp[0][i] = price[0][i]

# 인접한 집과 색이 달라야 함! dp[i][0] = dp[i-1][1], dp[i-1][2] 중 min값 + price[i][0]
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + price[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + price[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + price[i][2]

print(min(dp[-1]))