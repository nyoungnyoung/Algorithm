from collections import deque, defaultdict
import sys

def bfs(s):
    # 시작지점 s에서부터 다른 노드들까지의 거리 l
    l = [0] * (N + 1)

    # 시작지점 큐에넣고 방문처리
    queue = deque([s])
    visited[s] = 1

    # 큐가 빌 때까지
    while queue:
        # 노드 꺼내오기
        node = queue.popleft()
        # node와 연결된 노드들 중에서  
        for next in graph[node]:
            # 방문한 적 없는 노드면
            if not visited[next]:
                # 방문처리하고 거리 갱신해주기
                l[next] = l[node] + 1
                queue.append(next)
                visited[next] = 1
    
    # 거리의 합 return
    return sum(l)

input = sys.stdin.readline
N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

idx, cnt = 0, 5001
# 1 ~ N 유저의 케빈 베이컨 수 구해보기
for i in range(1, N + 1):
    # visited배열 초기화
    visited = [0] * (N + 1)
    tmp = bfs(i)
    # 최솟값 갱신
    if tmp < cnt:
        idx = i
        cnt = tmp
print(idx)