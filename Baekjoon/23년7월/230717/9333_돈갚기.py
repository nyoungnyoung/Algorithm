import decimal

T = int(input())
for _ in range(T):
    R, B, M = map(decimal.Decimal, input().split())
    cnt = 0
    for i in range(1200):
        cnt += 1
        B = round((R + decimal.Decimal(100.0)) / decimal.Decimal(100.0) * B, 2) - M
        if B <= 0:
            break
    if cnt >= 1200:
        cnt = "impossible"
    print(cnt)