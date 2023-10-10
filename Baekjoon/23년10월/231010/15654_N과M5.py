import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 정렬해주기
lst.sort()

# 백트래킹함수
def backtracking(dep):
    if dep == M:
        print(*visited)
        return

    # lst의 수를 돌아보면서
    for n in lst:
        # 이미 뽑은 수면 continue
        if n in visited:
            continue
        visited.append(n)
        backtracking(dep + 1)
        visited.pop()

visited = []
backtracking(0)