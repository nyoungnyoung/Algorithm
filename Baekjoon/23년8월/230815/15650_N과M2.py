import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(combinations([i for i in range(1, N+1)], M))
for idx in lst:
    print(*idx)