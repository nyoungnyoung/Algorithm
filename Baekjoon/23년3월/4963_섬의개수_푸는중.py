import sys


while True:
    w, h = map(int, sys.stdin.readline().split())
    if not w and not h:
        break
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    print(graph)