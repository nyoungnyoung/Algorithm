import sys

input = sys.stdin.readline

n,m = map(int, input().split())
lst = []

def dfs(start):
    if len(lst)==m:
        print(*lst)
        return
    
    for i in range(start, n+1):
        lst.append(i)
        dfs(i)
        lst.pop()
    
dfs(1)