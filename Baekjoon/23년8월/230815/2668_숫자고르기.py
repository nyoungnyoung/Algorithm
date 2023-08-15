import sys
from collections import defaultdict
input = sys.stdin.readline


def dfs(s, route):
    # 시작지점 route에 넣고 방문처리
    route.add(s)
    visited[s] = 1
    # 시작지점과 연결된 노드 중
    for node in graph[s]:
        # 방문한 적 없는 곳에서 dfs 수행
        if node not in route:
            dfs(node, route.copy())
        # 이미 방문한적 있는 경우(사이클이 생김)
        else:
            result.extend(list(route))
            return


# 입력받기
N = int(input().strip())
graph = defaultdict(list)
for i in range(1, N+1):
    graph[int(input().strip())].append(i)

visited = [0] * (N + 1)
result = []
# 1부터 N+1번 노드까지 방문한적 없는 노드에서 dfs 수행
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, set([]))

# result 개수 출력
print(len(result))

# result에 뽑힌 숫자 오름차순으로 출력하기
result.sort()
for i in result:
    print(i)