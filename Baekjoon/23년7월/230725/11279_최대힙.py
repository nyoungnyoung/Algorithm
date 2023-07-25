import heapq
import sys
input = sys.stdin.readline

# 파이썬의 heapq모듈은 최소힙 기준 -> 부호를 바꿔 최소힙을 최대힙처럼 활용
heap = []

N = int(input())
for _ in range(N):
    x = int(input())
    # x가 0이고 heap이 비어있지 않으면 힙에서 가장 큰 값 출력
    if not x:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    # x가 자연수면 x 추가
    if x > 0:
        heapq.heappush(heap, -x)