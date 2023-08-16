import sys
from heapq import heappush, heappop
input = sys.stdin.readline


N = int(input().strip())
heap = []
for _ in range(N):
    x = int(input().strip())
    if x:
        heappush(heap, (abs(x), x))
    else:
        try:
            print(heappop(heap)[1])
        except:
            print(0)