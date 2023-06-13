graph = [list(map(int, input().split())) for _ in range(9)]
max_n, max_i, max_j = 0, 0, 0
# 행렬 돌면서 최댓값과 (i, j)좌표 구하기
for i in range(9):
    for j in range(9):
        if max_n <= graph[i][j]:
            max_n = graph[i][j]
            # 행, 열이 1번부터 시작하므로 index에 +1 해줘야함!
            max_i, max_j = i+1, j+1
print(max_n)
print(max_i, max_j)