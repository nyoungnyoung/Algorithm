import sys

dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

# 함수 그대로 구현하기!
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    # dp[a][b][c]가 이미 존재하면 그 값을 return 
    if dp[a][b][c]:
        return dp[a][b][c]
    # 똑같은 값 계속 계산하지 않도록 dp에 저장해주기
    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]


while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    result = w(a, b, c)
    print(f'w({a}, {b}, {c}) = {result}')
    