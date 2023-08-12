import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = set(graph[0][0])
result = 0


def dfs(i, j, cnt):
    global result

    result = max(cnt, result)

    for d in range(4):
        ni = i + dx[d]
        nj = j + dy[d]

        # nx, ny가 범위 내에 있고, 지나온 적 없는 알파벳이면 dfs 탐색
        if 0 <= ni < R and 0 <= nj < C:
            if graph[ni][nj] not in visited:
                visited.add(graph[ni][nj])
                dfs(ni, nj, cnt + 1)
                visited.remove(graph[ni][nj])


dfs(0, 0, 1)
print(result)