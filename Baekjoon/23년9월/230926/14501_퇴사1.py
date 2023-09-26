import sys
input = sys.stdin.readline

N = int(input().strip())
lst = [list(map(int, input().split())) for _ in range(N)]

# Bottom-up 방식
dp = [0] * (N + 1)
for i in range(N):
    for j in range(i + lst[i][0], N + 1):
        if dp[j] < dp[i] + lst[i][1]:
            dp[j] = dp[i] + lst[i][1]

print(dp[-1])

# Top-down 방식(뒤에서부터 살펴보기)
dp2 = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    # i일에 상담을 했을 때 퇴사일을 넘어갈 경우 i일에 상담하지 않음
    if i + lst[i][0] > N:
        dp2[i] = dp2[i + 1]
    else:
        # i일에 상담 하는 것과 하지 않는 것 중 더 큰 값 저장 
        dp2[i] = max(dp2[i + 1], lst[i][1] + dp2[i + lst[i][0]])

print(dp2[0])