import sys
input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))
# m번 반복해서 카드 합체
for _ in range(m):
    # 카드의 숫자를 오름차순으로 정렬하고 가장 작은 수 두개를 x, y로 설정
    card.sort()
    card[0] += card[1]
    card[1] = card[0]
print(sum(card))
