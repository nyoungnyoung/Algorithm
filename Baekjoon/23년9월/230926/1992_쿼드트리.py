import sys
input = sys.stdin.readline

def dfs(i, j, N):
    color = graph[i][j]
    for ni in range(i, i + N):
        for nj in range(j, j + N):
            if color != graph[ni][nj]:
                print("(", end="")
                dfs(i, j, N // 2)
                dfs(i, j + N // 2, N // 2)
                dfs(i + N // 2, j, N // 2)
                dfs(i + N // 2, j + N // 2, N // 2)
                print(")", end="")
                return
    # if문 안걸리고 for문 종료 -> 종이 하나가 전부 같은 색이라는 뜻
    print(1 if color else 0, end="")

N = int(input().strip())
graph = [list(map(int, input().strip())) for _ in range(N)]
dfs(0, 0, N)