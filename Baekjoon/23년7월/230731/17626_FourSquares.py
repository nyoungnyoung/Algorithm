import sys
input = sys.stdin.readline

N = int(input().strip())
dp = [0] * (N + 1)
dp[1] = 1

# 나머지 애들 dp값 점화식을 통해 구해주기
for i in range(2, N+1):
    min_n = sys.maxsize

    # N의 제곱근보다 작은 자연수들의 dp값 탐색!
    for j in range(1, int(i ** 0.5) + 1):
        min_n = min(min_n, dp[i - (j ** 2)])
    dp[i] = min_n + 1

print(dp[N])