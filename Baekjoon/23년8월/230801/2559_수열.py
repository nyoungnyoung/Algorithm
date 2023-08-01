import sys
input = sys.stdin.readline

N, K = map(int, input().split())
degree = list(map(int, input().split()))

# tmp: 0 ~ K-1 합
tmp = sum(degree[:K])
result = tmp

# 오른쪽 인덱스 값은 더하고, 왼쪽 인덱스 값은 빼주며 result 갱신 
for i in range(K, N):
    tmp += degree[i] - degree[i - K]
    result = max(tmp, result)

print(result)