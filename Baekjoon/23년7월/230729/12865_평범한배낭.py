import sys
input = sys.stdin.readline


N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
items = [(0, 0)]
# 물건 리스트에 담아주기
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))
# dp로 최대값 구하기! 행 : 물건 개수 1 ~ N
for i in range(1, N + 1):
    # items 배열에서 w, v 가져오기
    w, v = items[i]
    # 열 : 배낭 크기 1~k
    for j in range(1, K + 1):
        # 현재 확인하는 물건의 무게가 배낭 크기가 더 작으면 물건을 넣지 않아야함
        if j < w:
            dp[i][j] = dp[i - 1][j]
        # 그렇지 않은 경우 현재 확인하는 물건을 (넣거나/안넣거나)로 나누어서 해당 경우 중 max값 dp에 저장 
        else:
            # 현재 물건을 넣는 경우 : 현재무게(v) + 남은 무게를 이전 물건으로 채울 때 최대 가치
            # 현재 물건을 넣지 않는 경우 : 이전 물건들로 현재 무게를 채울 때 최대 가치
            dp[i][j] = max(v+ dp[i - 1][j - w], dp[i - 1][j])

# N, K일 때 최대 가치 출력            
print(dp[N][K])