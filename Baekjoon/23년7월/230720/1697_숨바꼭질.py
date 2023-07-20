import sys
from collections import deque

def bfs(s):
    # 시작지점 넣은 상태로 큐 만들어주기
    queue = deque([s])
    # 큐가 빌 때 까지
    while queue:
        # 다음 방문지점 큐에서 뽑아오기
        node = queue.popleft()
        # node가 동생 위치랑 같아지면 visited[node] return
        if node == K:
            return visited[node]
        # 노드에서 방문할 수 있는 곳 방문
        for next in (node - 1, node + 1, 2 * node):
            # 범위 내이고 방문한적 없는 곳이면
            if 0 <= next < 100001 and not visited[next]:
                # 이전 지점에 적혀있던 숫자에 + 1 해주고 큐에 넣어주기
                visited[next] = visited[node] + 1
                queue.append(next)


N, K = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(100001)]
print(bfs(N))

