from collections import deque

N = int(input())
M = int(input())
lst = [[] for _ in range(N+1)]              # 인접리스트
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    # 인접리스트 저장
    lst[a].append(b)
    lst[b].append(a)

cnt = 0

# dfs(재귀)
def dfs(start):
    global cnt
    visited[start] = 1
    for node in lst[start]:     # 시작노드와 연결된 노드 중
        if not visited[node]:   # 방문하지 않은 노드를
            dfs(node)           # 재귀 탐색
            cnt += 1            # 연결되어있다면 바이러스에 걸리는 컴퓨터

dfs(1)
print(cnt)