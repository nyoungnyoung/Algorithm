import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    lst = list(map(int, input().split()))

    max_p = 0
    result = 0

    for i in range(N - 1, -1, -1):
        if lst[i] > max_p:
            max_p = lst[i]
        else:
            result += max_p - lst[i]

    print(result)