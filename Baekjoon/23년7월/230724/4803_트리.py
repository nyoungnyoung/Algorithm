import sys
input = sys.stdin.readline

# union 함수
def union(n, m):
    n = find(n)
    m = find(m)
    # 각 노드의 부모노드를 찾아서(find) 더 작은 값으로 통일시켜주기
    if n < m:
        parent[m] = n
    else:
        parent[n] = m

# find 함수
def find(n):
    # n이 부모노드(대표노드)가 아니면 find 다시 수행하며 parent배열 업데이트
    if n != parent[n]:
        parent[n] = find(parent[n])
    # if문에 안걸릴 때 parent[n] 리턴 
    return parent[n]

case = 0
# 0 0 입력 받기 전까지 계속 반복
while True:
    case += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    # 부모 노드 배열, 사이클 노드 set 선언
    parent = [i for i in range(n + 1)]
    cycle = set()
    # 트리 간선 입력받기
    for _ in range(m):
        a, b = map(int, input().split())

        # 입력 받을 때 마다 사이클 존재하는지(부모노드가 같으면) 판단해주기
        if find(a) == find(b):
            # 사이클에 각 노드의 대표노드 넣어주기
            cycle.add(parent[a])
            cycle.add(parent[b])
        # 둘 중 하나가 사이클에 포함되있으면 둘다 사이클에 포함됨
        if parent[a] in cycle or parent[b] in cycle:
            cycle.add(parent[a])
            cycle.add(parent[b])
        # if문에 안걸리면 union해주기
        union(a, b)
    
    # 마지막 간선까지 대표노드 통일
    for i in range(n + 1):
        find(i)

    # 대표노드들 중 사이클에 포함되지 않는 노드의 개수가 트리의 개수!
    parent = list(set(parent))        # 중복제거
    cnt = -1                          # 0노드 제외
    for p in parent:
        if p not in cycle:
            cnt += 1
    
    if cnt == 0:
        print(f'Case {case}: No trees.')
    elif cnt == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {cnt} trees.')