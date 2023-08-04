from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [0] * 100001

queue = deque([N])
graph[N] = 1
while queue:
    now = queue.popleft()
    if now == K:
        print(graph[K] - 1)
        break
    # 현재 위치에서 갈 수 있는 위치로 모두 이동해보기
    for next in (2 * now, now - 1, now + 1):
        # 범위를 벗어나지 않고 방문한적 없는 곳이라면
        if 0 <= next < 100001 and graph[next] == 0:
            # 순간이동하는 경우
            if next == 2 * now:
                graph[next] = graph[now]
                queue.appendleft(next)
            # 걸어가는 경우
            else:
                graph[next] = graph[now] + 1
                queue.append(next)