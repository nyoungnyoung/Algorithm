from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    cnt = 1
    queue = deque([(i, j)])
    visited[i][j] = 1
    
    # 큐가 빌때까지
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 탐색
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]

            # nx, ny가 범위를 벗어나지 않고
            if 0 <= nx < n and 0 <= ny < m:
                # 방문한적 없는 1일때(그림일 때)
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

pic, max_c = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            pic += 1
            max_c = max(max_c, bfs(i, j))

print(pic)
print(max_c)
