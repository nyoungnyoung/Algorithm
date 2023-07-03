import sys

# ㅗ 모양 제외 계산해주는 함수


def dfs(i, j, cnt, val):
    global result
    # 4번 돌고나면 result와 val에 저장된 값 중 더 큰 값으로 result 업데이트 후 return
    if cnt == 4:
        result = max(result, val)
        return

    for d in delta:
        ni = i + d[0]
        nj = j + d[1]
        # ni, nj가 범위 내에 있고 방문한 적 없으면
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            # 방문 표시 후 dfs 수행, 다시 visited 초기화
            visited[ni][nj] = 1
            dfs(ni, nj, cnt + 1, val + paper[ni][nj])
            visited[ni][nj] = 0

# ㅗ 모양 계산해주는 함수


def other(i, j):
    global result
    for k in range(4):
        now = paper[i][j]
        # now를 중심으로 3개씩만 돌아보면 ㅗ 모양 만들수 있음
        for l in range(3):
            m = (k + l) % 4
            ni = i + delta[m][0]
            nj = j + delta[m][1]
            # ni, nj가 범위 내에 있으면 now에 값 더해주기
            if 0 <= ni < N and 0 <= nj < M:
                now += paper[ni][nj]
            # 아니면 break
            else:
                break
        result = max(result, now)


# 상/하/좌/우 델타 선언
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = 0

# 돌아보면서 dfs, other 함수 실행
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, paper[i][j])
        visited[i][j] = 0
        other(i, j)

print(result)


# 다른 사람 코드(dfs와 other을 하나의 함수로 통합)
# ✨ 입력
# import sys
# input = sys.stdin.readline
# N,M = map(int,input().split())
# board = [list(map(int,input().split())) for _ in range(N)]
# visit = [[0]*M for _ in range(N)]

# dx = [-1,0,1,0]
# dy = [0,-1,0,1]

# # ✨ DFS
# def DFS(x,y,L,total):
#     global res
#     if res >= total + max_pos*(4-L):
#         return # ✨ 예외처리
#     if L == 4:
#         res = max(res,total)
#         return # ✨ 4칸을 돌면 == 테트로미노를 만들면
#     else:
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<N and 0<=ny<M and visit[nx][ny] == 0:
#                 if L == 2: # ✨ 2번째 테트로미노에서
#                     visit[nx][ny] = 1
#                     DFS(x,y,L+1,total+board[nx][ny])
#                     visit[nx][ny] = 0
#                 visit[nx][ny] = 1
#                 DFS(nx,ny,L+1,total+board[nx][ny])
#                 visit[nx][ny] = 0
            
# # ✨ 준비
# max_pos = max(map(max,board)) 
# res = 0
# for i in range(N):
#     for j in range(M):
#         visit[i][j] = 1
#         DFS(i,j,1,board[i][j])
#         visit[i][j] = 0
# print(res)