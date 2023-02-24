from collections import deque

N = int(input())
M = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]     # 인접행렬
visited = []
for _ in range(M):
    a, b = map(int, input().split())
    # 인접행렬 저장
    arr[a][b], arr[b][a] = 1, 1
print(arr)


def dfs(start):
    
    return