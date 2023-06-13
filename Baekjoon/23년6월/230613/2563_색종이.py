graph = [[0] * 101 for _ in range(101)]
# 색종이 붙이기
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    # 시작점부터 10*10구간 검은색(1)으로 칠해주기
    for i in range(x, x+10):
        for j in range(y, y+10):
                graph[i][j] = 1
# 1 개수 세주기
cnt = 0
for i in range(101):
    for j in range(101):
        if graph[i][j]:
            cnt += 1
print(cnt)