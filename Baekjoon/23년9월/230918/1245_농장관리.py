import sys

input = sys.stdin.readline

def dfs(i, j):
    stack.append((i, j))
    flag = True
    while stack:
        x, y = stack.pop()
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[i][j] < graph[nx][ny]:
                    flag = False
                if not visited[nx][ny] and graph[nx][ny] == graph[i][j]:
                    stack.append((nx, ny))
                    visited[nx][ny] = 1
    if flag:
        return True
    return False

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
cnt = 0
stack = []

for i in range(N):
    for j in range(M):
        if not visited[i][j] and dfs(i, j):
            cnt += 1

print(cnt)