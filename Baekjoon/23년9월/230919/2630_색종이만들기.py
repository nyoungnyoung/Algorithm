import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

# 하나의 종이가 모두 같은 색인지 판별
def dfs(i, j, N):
    global cnt_w, cnt_b
    # 첫 지점의 색 확인
    color = paper[i][j]
    # 탐색 하면서 첫 지점의 색과 같은지 확인해주기 
    for ni in range(i, i + N):
        for nj in range(j, j + N):
            # paper[ni][nj]가 첫 지점의 색과 같지 않으면 4개로 분할해서 탐색
            if paper[ni][nj] != color:
                dfs(i, j, N//2)
                dfs(i, j + N//2, N//2)
                dfs(i + N//2, j, N//2)
                dfs(i + N//2, j + N//2, N//2)
                return
    # if문에 안걸리면 종이가 모두 같은색인거! 무슨색인지 판단
    if color == 0:
        cnt_w += 1
    else:
        cnt_b += 1


N = int(input().strip())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt_w, cnt_b = 0, 0
dfs(0, 0, N)
print(cnt_w)
print(cnt_b)