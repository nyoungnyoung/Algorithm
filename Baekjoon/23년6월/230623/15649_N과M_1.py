from itertools import permutations

N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]
per = list(permutations(lst, M))
for i in per:
    print(*i)
