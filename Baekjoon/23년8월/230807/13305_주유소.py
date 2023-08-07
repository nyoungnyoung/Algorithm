import sys
input = sys.stdin.readline

N = int(input())
roads = list(map(int,input().split()))
costs = list(map(int,input().split()))

min_price = roads[0] * costs[0]
min_cost = costs[0]

for i in range(1, N-1):
  if min_cost > costs[i]: 
    min_cost = costs[i]
  min_price += min_cost * roads[i]

print(min_price)