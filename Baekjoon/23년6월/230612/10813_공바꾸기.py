N, M = map(int, input().split())
# 각 바구니의 번호에 해당하는 공 넣어주기
basket = [i for i in range(1, N+1)]
# for 문 돌면서 공 바꾸기 진행
for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
print(*basket)
