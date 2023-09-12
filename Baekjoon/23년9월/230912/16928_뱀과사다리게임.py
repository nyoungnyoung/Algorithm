from collections import deque, defaultdict
import sys

input = sys.stdin.readline

# 1 ~ 6 주사위, 100 * 100 보드판
# 주사위를 굴려 나온 수만큼 이동 -> 주사위를 굴린 결과가 100번칸을 넘어가면 이동할 수 없음
# 도착한 칸이 사다리면 사다리르 타고 위로 올라감
# 뱀이 있는 칸에 도착하면 뱀을 따라 내려감
# 1번칸 -> 100번칸에 도착하는 것이 목표
# 몇번의 주사위를 굴려야하는지 그 최솟값을 구하는게 목표!

def bfs():
    # 1번칸 큐에 넣고 방문처리
    queue = deque([1])
    visited[1] = 1
    # 큐가 빌 때까지
    while queue:
        # 현재 위치 큐에서 뽑아오고
        now = queue.popleft()
        # 거기서부터 방문할 수 있는 칸(now + 주사위에 적힌 1 ~ 6) 탐색
        for d in range(1, 7):
            next = now + d
            # next가 범위 내에 있고 아직 방문한 적 없어야 함
            if 0 < next <= 100 and not visited[next]:
                # next에 사다리가 있으면 사다리 타고 이동
                if next in ladder.keys():
                    next = ladder[next]
                # next에 뱀이 있으면 뱀 타고 이동
                if next in snake.keys():
                    next = snake[next]
                # 이동 후에도 next에 방문한적 없다면 next 큐에 넣고 방문처리, graph에 이동횟수 갱신해주기
                if not visited[next]:
                    queue.append(next)
                    visited[next] = 1
                    graph[next] = graph[now] + 1


N, M = map(int, input().split())
graph = [0] * 101
visited = [0] * 101

ladder = defaultdict(int)
snake = defaultdict(int)
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

bfs()
print(graph[100])