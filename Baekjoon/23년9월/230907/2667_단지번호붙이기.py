import sys

input = sys.stdin.readline

def dfs(i, j):
    global cnt
    # 첫 지점 방문처리 후 스택에 넣기
    visited[i][j] = 1
    stack = [(i, j)]
    tmp = 1
    
    # 스택이 빌 때까지
    while stack:
        # 스택에서 좌표 pop
        x, y = stack.pop()
        # 다음 좌표 델타 탐색
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]
            # (nx, ny)가 범위를 벗어나지 않고, 방문된적 없고, 1이면 
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny]:
                # (nx, ny) 방문처리 & 스택에 넣고 tmp + 1
                visited[nx][ny] = 1
                stack.append((nx, ny))
                tmp += 1
    
    # 스택이 비면 하나의 단지 dfs 완료, cnt + 1
    cnt += 1
    result.append(tmp)
    

N = int(input().strip())
graph = [list(map(int, input().strip())) for _ in range(N)]
# 델타 선언
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[0] * N for _ in range(N)]
result = []
cnt = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            dfs(i, j)
print(cnt)
result.sort()
for i in result:
    print(i)