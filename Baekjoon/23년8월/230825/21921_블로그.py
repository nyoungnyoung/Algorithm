import sys
input = sys.stdin.readline

N, X = map(int, input().split())
today = list(map(int, input().split()))

# 1~X일 방문자수 합 tmp에 저장
tmp = sum(today[:X])
result = tmp
cnt = 1

# 양 끝값 더하고 빼주면서 확인해주기
for i in range(X, N):
    # 왼쪽 끝값 빼고 오른쪽 끝값 더해주기
    tmp = tmp - today[i - X] + today[i]
    # result값과 비교해 tmp값이 더 크면 갱신
    if result < tmp:
        result = tmp
        cnt = 1
    # result값과 tmp값이 같으면 cnt+1
    elif result == tmp:
        cnt += 1

if not result:
    print('SAD')
else:
    print(result)
    print(cnt)
