import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

def dfs(s):
    global num
    visited[s] = num            # 시작지점 방문처리
    for i in sorted(graph[s]):  # 시작지점과 이어진 노드 오름차순으로 탐색
        if not visited[i]:      # 방문한적 없으면
            num += 1            # num에 +1
            dfs(i)              # dfs 수행

N, M, R = map(int, input().split())
graph = defaultdict(list)
visited = [0] * (N + 1)
num = 1

# 인접 리스트 생성
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# R번부터 시작해서 DFS 탐색
dfs(R)

# 1번부터 N번 노드까지 방문순서 출력
for i in range(1, N + 1):
    print(visited[i])