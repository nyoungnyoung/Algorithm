T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input()))
    cnt = {}
    for i in card:
        if i not in cnt:
            cnt[i] = 1
        else:
            cnt[i] += 1
    print(max(cnt))
    print(cnt)
    # print(card)
    print(f'#{tc}')