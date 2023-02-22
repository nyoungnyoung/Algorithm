import sys
N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [[0] * M for _ in range(N)]
for i in range(N):
    if i != 0: print()
    for j in range(M):
        print(A[i][j] + B[i][j], end=" ") 
        
# 다른사람 코드
# N, M = map(int, input().split())
# p=[]
# for i in range(N*2):
#     p.append(list(map(int,input().split())))
# for i in range(N):
#     for j in range(M):
#         print(p[i][j] + p[i+N][j], end=" ")
#     print()