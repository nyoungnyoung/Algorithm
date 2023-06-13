N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

# A행렬과 B행렬의 원소 더해주기
for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]
for i in range(N):
    print(*A[i])

