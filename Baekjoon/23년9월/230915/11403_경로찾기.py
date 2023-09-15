import sys
input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]

# 경유지 k, 출발노드 s, 도착노드 e
for k in range(N):
    for s in range(N):
        for e in range(N):
            if graph[s][k] and graph[k][e]:
                graph[s][e] = 1

for i in range(N):
    print(*graph[i])