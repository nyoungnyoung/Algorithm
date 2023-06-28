import sys
N, X = map(int, sys.stdin.readline().split())
price = list(map(int, sys.stdin.readline().split()))
s, e = 0, 1
min_p = sys.maxsize
while e < N:
    if price[s] * X + price[e] * X < min_p:
        min_p = price[s] * X + price[e] * X
    s += 1
    e += 1
print(min_p)