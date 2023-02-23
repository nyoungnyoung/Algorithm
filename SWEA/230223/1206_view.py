for tc in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    result = 0
    for i in range(2, N-2):
        max_h = 0
        for j in range(i-2, i+3):
            if i == j:
                continue
            if max_h < building[j]:
                max_h = building[j]
        if max_h < building[i]:
            result += building[i] - max_h
    print(f'#{tc} {result}')