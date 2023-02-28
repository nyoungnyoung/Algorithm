from collections import deque

# dfs(재귀)
def dfs(start):
    global cnt_dfs
    visited[start] = 1
    for node in lst[start]:     # 시작노드와 연결된 노드 중
        if not visited[node]:   # 방문하지 않은 노드를
            dfs(node)           # 재귀 탐색
            cnt_dfs += 1        # 연결되어있다면 바이러스에 걸리는 컴퓨터

# dfs(스택)
def dfs_stack(start):
    visited, stack = [], [start]
    visited.append(start)               # 시작지점 방문처리
    while stack:                        # 스택이 빌때까지 반복해서
        node = stack.pop()              # 노드를 꺼내온 뒤
        for v in lst[node]:             # 노드와 연결된 다른 노드에
            if v not in visited:        # 방문한적 없으면
                visited.append(v)       # 방문처리 후
                stack.append(v)         # 스택에 넣어준다
    return len(visited) - 1

N = int(input())
M = int(input())
lst = [[] for _ in range(N+1)]              # 인접리스트

for _ in range(M):
    a, b = map(int, input().split())
    # 인접리스트 저장
    lst[a].append(b)
    lst[b].append(a)



cnt_dfs = 0
visited = [0] * (N+1)
dfs(1)
print(cnt_dfs)
print(dfs_stack(1))     # dfs(스택) 정답

# visited = [0] * (N+1)