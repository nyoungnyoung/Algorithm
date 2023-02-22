from collections import deque
import sys

# dfs 재귀로 구현
def dfs(start):
    visited[start] = True   # 시작점 방문처리
    print(start, end=" ")   # 출력
    for i in graph[start]:  # start와 연결된 노드i 탐색
        if not visited[i]:  # i를 방문한적 없으면
            dfs(i)          # i를 시작점으로 다시 dfs탐색
    
# bfs
def bfs(start):
    queue = deque([start])  # 큐에 시작점 넣기
    visited[start] = True   # 시작점 방문처리
    while queue:            # 큐가 빌 때까지 반복
        node = queue.popleft()      # 큐에서 다음 탐색 노드 꺼내오기
        print(node, end=" ")
        for i in graph[node]:       # node와 연결된 노드 i 탐색
            if not visited[i]:      # i를 방문한 적 없으면
                visited[i] = True   # i 방문처리하고
                queue.append(i)     # 큐에 i를 넣어준다!

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]   # 인접리스트 생성

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()    

visited = [0] * (N + 1)
dfs(V)
print()
visited = [0] * (N + 1)
bfs(V)