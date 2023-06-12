chess = [1, 1, 2, 2, 2, 8]
check = list(map(int, input().split()))
# 6개 모두 확인해보기
for i in range(6):
    chess[i] = chess[i] - check[i]
print(*chess)
