import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
p = [0 for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
# 인접리스트로 트리 데이터 저장
tree = defaultdict(list)
# 자식노드로 가기 직전에 현재 노드가 다음번에 탐색할 미방문 노드의 부모노드임
for _ in range(1, N):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# dfs함수
def dfs(n):
    # 방문처리 해주기
    visited[n] = 1
    # 현재 노드와 연결된 노드 중에서 방문하지 않은 노드에서 dfs 수행
    for node in tree[n]:
        if not visited[node]:
            # 이 때 n이 node의 부모노드!
            p[node] = n
            dfs(node)

# 루트노드 1부터 dfs 수행
dfs(1)

# 2번노드부터 p 배열 출력
for i in range(2, N + 1):
    print(p[i])