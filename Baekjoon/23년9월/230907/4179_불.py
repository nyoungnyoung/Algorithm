from collections import deque
import sys

input = sys.stdin.readline

def bfs_f():
    # 큐가 빌때까지 불이 퍼지게 만들기
    while fq:
        x, y = fq.popleft()
        # 상하좌우로 불 이동
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]
            # nx, ny가 범위 내에 있고
            if 0 <= nx < R and 0 <= ny < C:
                # graph[nx][ny]가 벽이 아니면서 방문한적 없는 곳이면
                if not fire[nx][ny] and graph[nx][ny] != '#':
                    # +1 방문처리 & 큐에 넣어주기
                    fire[nx][ny] = fire[x][y] + 1
                    fq.append((nx, ny))

def bfs_j():
    # 큐가 빌때까지 지훈이 움직여보기
    while jq:
        x, y = jq.popleft()
        # 상하좌우로 지훈이 이동
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]
            # (nx, ny) 가 범위를 벗어나면 지훈이 탈출한거! jihoon[x][y] 출력 후 return
            if not (0 <= nx < R and 0 <= ny < C):
                print(jihoon[x][y])
                return
            # graph[nx][ny]가 벽이 아니면서 지훈이가 방문한 적 없는 곳이라면
            if graph[nx][ny] != '#' and not jihoon[nx][ny]:
                # 불이 퍼지지 않은 곳이나, 불이 퍼진 시간보다 이동한 시간이 짧아야 갈 수 있음
                if not fire[nx][ny] or jihoon[x][y] + 1 < fire[nx][ny]:
                    # +1로 갱신 & 큐에 넣어주기
                    jihoon[nx][ny] = jihoon[x][y] + 1
                    jq.append((nx, ny))
    # return에 안걸리고 while문 종료되면 탈출 불가
    print('IMPOSSIBLE')
    return
    

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
fire = [[0] * C for _ in range(R)]
jihoon = [[0] * C for _ in range(R)]
fq = deque()
jq = deque()
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 불/지훈 위치 저장
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':
            fq.append((i, j))
            fire[i][j] = 1
        elif graph[i][j] == 'J':
            jq.append((i, j))
            jihoon[i][j] = 1
# 불의 이동경로 bfs 탐색 후 지훈이 bfs 탐색하기
bfs_f()
bfs_j()
