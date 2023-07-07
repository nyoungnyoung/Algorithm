import sys
from collections import deque


def bfs(i, j):
    # 상/하/좌/우 델타
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(i, j)])
    visited[i][j] = 0

    while queue:
        x, y = queue.popleft()

        # 상하좌우 델타탐색
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]

            # ni, nj가 범위 내에 있고 방문한 적 없으면
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                # 갈 수 없는 곳이면 0 표시
                if not graph[nx][ny]:
                    visited[nx][ny] = 0
                # 갈수 있는 땅이면 이전에 표시한 값에 + 1
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

# 출발지점 인덱스 확인
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
