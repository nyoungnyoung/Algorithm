import sys
N = int(sys.stdin.readline().strip())
min_x = min_y = 10000
max_x = max_y = -10000
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y
print(abs(max_x - min_x) * abs(max_y - min_y))
