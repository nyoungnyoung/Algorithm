T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input()))
    counts = [0] * 10           # 0~9까지 숫자 개수 세어줄 배열
    for i in lst:               # lst의 원소를 돌아보면서
        counts[i] += 1          # 숫자 세주기!
    max_card, max_num = 0, 0    # 가장 많은 카드 갯수, 카드에 적힌 숫자 
    for i in range(10):
        if max_card <= counts[i]:
            max_card = counts[i]
            max_num = i
    print(f'#{tc} {max_num} {max_card}')