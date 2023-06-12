N, M = map(int, input().split())
# 바구니 만들기
basket = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    # 0~i-1번째 바구니 +  i-1~j-1번까지의 바구니를 뒤집은 것 + j~마지막 바구니
    basket = basket[:i-1] + basket[i-1:j][::-1] + basket[j:]
print(*basket)

# 시간 효율을 위해 reverse보다는 lst slicing을 사용하도록 하자!
