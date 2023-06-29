import sys
from collections import deque


def bfs(i, j):
    # 상하좌우 델타 선언
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue.append((i, j))
    # 큐가 빌 때 까지
    while queue:
        # 큐에서 칸 인덱스 하나 빼서
        x, y = queue.popleft()
        # 해당 칸이랑 인접한 칸들 중에서 이동할 수 있는 칸 방문처리 해주기
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    # 제일 마지막 칸에 적히는 숫자 return
    return graph[N-1][M-1]


N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
queue = deque()
print(bfs(0, 0))
