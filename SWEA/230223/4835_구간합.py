T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    min_sum, max_sum = float('inf'), 0      # min, max값에 임의의 큰수와 작은수 할당
    for i in range(N-M+1):
        tmp = 0
        for j in range(i, i+M):
            tmp += lst[j]
        if min_sum > tmp:
            min_sum = tmp
        if max_sum < tmp:
            max_sum = tmp
    print(f'#{tc} {max_sum - min_sum}')