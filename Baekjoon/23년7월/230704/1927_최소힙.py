from heapq import heappop, heappush
import sys

arr = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if not x:
        if not arr:
            print(0)
        else:
            print(heappop(arr))
    else:
        heappush(arr, x)
