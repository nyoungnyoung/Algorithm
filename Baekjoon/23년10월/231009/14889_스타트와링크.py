import sys
input = sys.stdin.readline

N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]
visitied = [0] * N
result = 10 ** 7

def dfs(dep, idx):
    global result
    # 선수 중 절반을 탐색하면 나머지 절반은 다른팀!
    if dep == N // 2:
        A, B = 0, 0
        for i in range(N):
            for j in range(N):
                # i, j 모두 방문처리된 선수면 A팀에
                if visitied[i] and visitied[j]:
                    A += board[i][j]
                # 둘다 방문처리 되지 않은 선수면 B팀에 넣기
                elif not visitied[i] and not visitied[j]:
                    B += board[i][j]
        # result 업데이트해주기
        result = min(result, abs(A - B))
        return
    # if문에 안걸리면 현재선수의 idx부터 N까지 돌면서
    for i in range(idx, N):
        # 방문처리되어있지 않은 선수면
        if not visitied[i]:
            visitied[i] = 1
            dfs(dep + 1, i + 1)
            visitied[i] = 0

dfs(0, 0)
print(result)
