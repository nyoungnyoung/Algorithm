T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    result = max(lst) - min(lst)
    print(f'#{tc} {result}')