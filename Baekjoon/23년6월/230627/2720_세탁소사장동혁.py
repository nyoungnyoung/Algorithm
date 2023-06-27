T = int(input())
for _ in range(T):
    # 앞에서부터 차례차례 최대개수 저장해주면 됨!
    money = {25: 0, 10: 0, 5: 0, 1: 0}
    C = int(input())
    for i in money:
        money[i] = C // i
        C %= i
    print(*money.values())