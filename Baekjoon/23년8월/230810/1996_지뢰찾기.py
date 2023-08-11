import sys
input = sys.stdin.readline

N = int(input())
graph = [input().strip() for _ in range(N)]

# 지뢰의 개수를 저장할 result 배열
result = [[0] * N for _ in range(N)]

# 8방향 델타
delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# 지뢰가 있는 칸을 찾아 인접해 있는 칸에 지뢰 개수를 더하자.
for i in range(N):
    for j in range(N):
        if graph[i][j].isdigit(): # 숫자라면 지뢰가 있는 칸
            n = int(graph[i][j])
            for di, dj in delta:
                if 0 <= i + di < N and 0 <= j + dj < N:
                    result[i + di][j + dj] += n

for i in range(N):
    for j in range(N):
        if graph[i][j].isdigit(): # 지뢰가 있는 칸
            print('*', end = '')
        elif result[i][j] >= 10: # 주위 지뢰가 10개 이상
            print('M', end = '')
        else: # 주위 지뢰가 10개 미만
            print(result[i][j], end = '')
    print()