import sys
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
blank = []

# 빈칸의 좌표 blank에 기록해주기
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

# 가로줄 확인
def row(i, x):
    # i행 0 ~ 8열 확인
    for n in range(9):
        # x가 이미 해당 행에 있으면
        if x == graph[i][n]:
            return False
    return True

# 세로줄 확인
def column(j, x):
    # 0 ~ 8 행 j열 확인
    for n in range(9):
        # x가 이미 해당 열에 있으
        if x == graph[n][j]:
            return False
    return True

# 3 X 3 칸 확인
def square(i, j, x):
    ni = i // 3 * 3
    nj = j // 3 * 3
    for n in range(3):
        for m in range(3):
            if x == graph[ni + n][nj + m]:
                return False
    return True

# dfs로 빈칸에 1 ~ 9까지 넣어보기
def dfs(n):
    # 빈 공간을 모두 채웠으면
    if n == len(blank):
        # 그래프 출력해주고 return
        for i in graph: 
            print(*i) 
        exit()

    # 빈칸에 1부터 9까지 넣어보자
    for x in range(1, 10):
        i, j = blank[n][0], blank[n][1]
        # 그 자리에 넣어도 되는 수면
        if column(j, x) and row(i, x) and square(i, j, x):
            # dfs 수행
            graph[i][j] = x
            dfs(n + 1)
            graph[i][j] = 0

dfs(0)