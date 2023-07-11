import sys
sys.setrecursionlimit(1000000)

def union(a, b):
    # a, b의 루트노드 찾기
    a = find(a)
    b = find(b)
    # a, b 의 루트노드 크기 비교해서 더 작은 걸 부모로 해서 합쳐주기
    if a < b:
        p[b] = a
    else:
        p[a] = b

def find(a):
    # 자기자신이 루트노드가 아니면 루트노드 찾아가기
    if a != p[a]:
        p[a] = find(p[a])
    # 자기 자신이 루트노드면 p[a] return
    return p[a]
    

n, m = map(int, sys.stdin.readline().split())
p = [i for i in range(n + 1)]

for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())
    # 명령이 0이면 union(a, b)
    if not c:
        union(a, b)
    # 명령이 1이면 find(a) find(b) 비교해서 동일한 집합인지 판단
    elif c == 1:
        # 동일한 집합이면 YES
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
