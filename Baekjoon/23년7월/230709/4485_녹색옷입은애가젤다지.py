import sys
from collections import deque
import heapq


def bfs(i, j):
    # 델타
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 첫 지점 큐에 넣고 visited에 기록해주기
    queue = deque([(i, j)])
    visited[0][0] = graph[0][0]

    # 큐가 빌때까지
    while queue:
        x, y = queue.popleft()

        # 상하좌우 탐색
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]

            # nx, ny가 범위 내에 있고,
            if 0 <= nx < N and 0 <= ny < N:
                # 최소비용인 걸 기록해주기
                if visited[nx][ny] > visited[x][y] + graph[nx][ny]:
                    visited[nx][ny] = visited[x][y] + graph[nx][ny]
                    queue.append((nx, ny))

    # 출구에 적혀있는 값 return
    return visited[N-1][N-1]


cnt = 0
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    cnt += 1
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [[int(1e9)] * N for _ in range(N)]
    result = bfs(0, 0)
    print(f'Problem {cnt}: {result}')
