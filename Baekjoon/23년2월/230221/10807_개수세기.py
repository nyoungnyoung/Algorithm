import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
cnt = 0
for i in lst:
    if i == v:
        cnt += 1
print(cnt)