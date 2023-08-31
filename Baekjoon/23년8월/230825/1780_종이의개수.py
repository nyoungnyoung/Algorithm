import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def cut():
    pass

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]
print(graph)
