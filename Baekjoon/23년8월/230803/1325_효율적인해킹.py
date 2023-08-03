from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(s):
    # 연결된 컴퓨터 수 세 주기 위해 cnt 설정, 방문배열 bfs 수행할때마다 초기화
    cnt = 1
    visited = [0] * (N + 1)
    # 시작지점 큐에 넣고 방문처리 해주기
    visited[s] = 1
    queue = deque([s])
    # 큐가 빌 때까지
    while queue:
        node = queue.popleft()
        # 현재 컴퓨터와 연결된 컴퓨터중
        for c in graph[node]:
            # 방문하지 않은 컴퓨터에서 bfs
            if not visited[c]:
                visited[c] = 1
                cnt += 1
                queue.append(c)
    # 마지막에 연결된 컴퓨터 개수 return
    return cnt
            

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

# 모든 컴퓨터에 대해 bfs 수행하며 연결된 컴퓨터 수가 최대인 컴퓨터 번호 저장
lst = []
max_n = 0

for i in range(1, N + 1):
    com = bfs(i)
    # print("bfs수행",i, com)
    # com이 기존 최댓값보다 크면 lst 초기화 시켜줘야함!
    if com > max_n:
        max_n = com
        lst.clear()
        lst.append(i)
    # com이 max_n과 같으면 lst에 추가
    elif com == max_n:
        lst.append(i)

print(*lst)