import sys 
sys.setrecursionlimit(10000) 

def dfs(x, y): 
    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1] 
    
    # 상,하,좌,우 확인 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0<= ny < M:
            if farm[nx][ny] == 1:
                farm[nx][ny] = -1
                dfs(nx, ny)
                
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    cnt = 0

    # 배추 심기
    for _ in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = 1

    # dfs 탐색하기
    for i in range(N):
        for j in range(M):
            if farm[i][j] > 0:
                dfs(i, j)
                cnt += 1
    print(cnt)
