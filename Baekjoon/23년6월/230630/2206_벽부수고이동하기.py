import sys
from collections import deque

def bfs(i, j, k):
    # 상/하/좌/우 델타 선언
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 시작지점 큐에 넣고 방문처리
    queue.append((i, j, k))
    visited[i][j][k] = 1
    while queue:
        # 큐에서 칸 하나 빼오기
        x, y, z = queue.popleft()
        # 마지막 지점에 도착 하면 해당 칸에 적혀있는 값 return
        if x == N - 1 and y == M - 1:
            return visited[x][y][z]
        # 해당 칸과 연결된 상/하/좌/우 연달아 두칸 탐색하기
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]
            # 일단 nx, ny가 범위 내에 있어야 함
            if 0 <= nx < N and 0 <= ny < M:
                # graph[nx][ny]가 벽이고, 아직 벽을 부수지 않았다면
                if graph[nx][ny] == 1 and z == 0:
                    # 방문처리 -> 벽 부순 거 표시!
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    # 큐에 넣을 때도 벽 부순 거 표시해주기
                    queue.append((nx, ny, 1))
                # graph[nx][ny]가 벽이 아니고, 방문한 적이 없는 곳이라면
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    # 방문 처리 후 큐에 넣어주기
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))
    # if문에 안걸리고 while문 종료되면 마지막 지점에 도달하지 못한 것
    return -1 

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
# 벽 부쉈는지 여부를 3차원 그래프로 표현, visited[x][y][0]은 벽 파괴 가능, visited[x][y][1]은 벽 파괴 불가능
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
queue = deque()
cnt = 1

print(bfs(0, 0, 0))
