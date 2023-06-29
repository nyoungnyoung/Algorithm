import sys
from collections import deque, defaultdict


def bfs(s):
    global cnt
    # 시작지점 방문처리
    visited[s] = cnt
    # 큐가 빌 때까지
    while queue:
        # 큐에서 노드 하나 뽑기
        node = queue.popleft()
        # 해당 노드와 연결된 방문하지 않은 노드들 오름차순으로 방문하며 큐에 삽입
        for i in sorted(graph[node]):
            if not visited[i]:
                # 방문 순서 + 1
                cnt += 1
                queue.append(i)
                visited[i] = cnt


N, M, R = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = [0] * (N+1)
queue = deque([R])
cnt = 1
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(R)
for i in range(1, N + 1):
    print(visited[i])
