X = int(input())
N = int(input())
cnt = 0         # 물건의 금액 합 저장해줄 변수
for _ in range(N):
    a, b = map(int, input().split())
    cnt += a*b
if cnt == X:
    print("Yes")
else:
    print("No")