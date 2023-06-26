import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

def dfs(s):
    # 재귀로 dfs 구현
    if visited[s]:
        return
    visited[s] = True           # 시작지점 방문처리
    for node in graph[s]:       # 시작지점과 연결된 노드 중
        if not visited[node]:   # 방문하지 않은 노드에서
            dfs(node)


N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = [False] * (N + 1)
cnt = 0
# 인접리스트 생성
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 1 ~ N번 노드 돌면서 방문한적 없는 노드에서 dfs 수행
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)