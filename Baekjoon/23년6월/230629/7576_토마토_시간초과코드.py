import sys
from collections import deque


def bfs(i, j):
    # 상/하/좌/우 델타 선언
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 시작지점 queue에 넣기
    queue.append((i, j))
    # 큐가 빌 때 까지 반복해서
    while queue:
        # 현재 칸의 인덱스 뽑기
        x, y = queue.popleft()
        # 상/하/좌/우 탐색
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]
            # nx, ny가 범위 내에 있고, tomato[nx][ny]가 -1이나 1이 아니면 토마토 익혀주기
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] != 1 and tomato[nx][ny] != -1:
                # tomato[x][y] + 1 한 값보다 tomato[nx][ny] 값이 크거나 tomato[nx][ny]가 0이면 덮어쓰기 해주면 됨
                if tomato[x][y] + 1 < tomato[nx][ny] or not tomato[nx][ny]:
                    queue.append((nx, ny))
                    tomato[nx][ny] = tomato[x][y] + 1


M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
queue = deque()
# 창고 돌면서 tomato[i][j]가 1인 곳에서 dfs 수행
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            bfs(i, j)

# 토마토 다 익었는지 확인
flag = True
# bfs로 다 돌았는데 값이 0인 곳이 있으면 안익은 토마토가 있다는 뜻
for lst in tomato:
    if 0 in lst:
        # flag 바꿔주기
        flag = False

if not flag:
    print(-1)
else:
    # 가장 큰 값 day에 저장
    day = max(max(tomato))
    if day == 1:
        print(0)
    else:
        print(day - 1)
