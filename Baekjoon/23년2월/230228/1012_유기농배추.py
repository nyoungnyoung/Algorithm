T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    print(farm)
