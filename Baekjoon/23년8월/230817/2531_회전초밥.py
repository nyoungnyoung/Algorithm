import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input().strip()) for _ in range(N)]
print(sushi)
# 벨트 위 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
# 초밥의 종류 하나가 쓰인 쿠폰 발행, 첫번째 행사에 참가하면 해당 쿠폰에 적힌 종류의 초밥을 무료로 제공
# 최대한 다양한 종류의 초밥을 먹으려고 할 경우

# 한 지점부터 시작해서 k개 살펴보며 겹치지 않게 k개 먹을 수 있는 경우 result에 저장
result = []
# 시작지점, 끝지점 인덱스 지정
s, e = 0, k
for i in range(N):
    # s~k 초밥 겹치지 않는지 확인
    tmp = set()
    for j in range(s, e):
        j %= N
        # 겹치지 않는 초밥이면 tmp에 추가해주기
        if sushi[j] not in tmp:
            tmp.add(sushi[j])
        # 겹치면 s, e 재조정 해주고 break
        else:
            s += 1
            e += 1
            break