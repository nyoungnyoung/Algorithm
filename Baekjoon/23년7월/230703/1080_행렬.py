import sys

# 행렬 뒤집는 함수


def flip(i, j, arr):
    for x in range(i, i+3):
        for y in range(j, j+3):
            arr[x][y] = 1 - arr[x][y]


N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
cnt = 0

# A, B를 돌아보면서 일치하지 않는 부분이 있으면 flip 실행
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            flip(i, j, A)
            cnt += 1

# A -> B 바꿀 수 있는지 확인(flip 다 하고나서 A랑 B가 같으면 바꿀수 있는거!)
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            cnt = -1
            break

if cnt >= 0:
    print(cnt)
else:
    print(-1)
