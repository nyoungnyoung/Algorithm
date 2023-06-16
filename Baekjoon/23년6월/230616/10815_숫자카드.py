import sys
N = int(sys.stdin.readline().strip())
card = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
check = list(map(int, sys.stdin.readline().split()))
result = [0 for _ in range(M)]
for i in range(len(check)):
    if check[i] in card:
        result[i] = 1
print(*result)
