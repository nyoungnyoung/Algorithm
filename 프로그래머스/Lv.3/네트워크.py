def dfs(n, computers, i, visited):
    visited[i] = 1      # 시작점 i 방문처리
    for j in range(n):  # 시작점과 연결된 컴퓨터 중 방문처리 되지 않은 컴퓨터 기준 dfs 재귀
        if j != i and computers[i][j]:
            if not visited[j]:
                dfs(n, computers, j, visited)

def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i, visited)
            answer += 1     # dfs 수행완료 할 때마다 네트워크 1개 추가
    return answer