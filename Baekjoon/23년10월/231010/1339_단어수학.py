from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input().strip())
words = [input().strip() for _ in range(N)]

# 각 단어들에 있는 알파벳 자리수에 맞게 딕셔너리에 저장해주기
alp = defaultdict(int)

for word in words:
    # 각 단어 하나씩 확인해주기
    for i in range(len(word)):
        # 단어가 세자리이면 첫째자리는 100의자리, 둘째자리는 10의자리, 셋째자리는 1의자리가 됨
        alp[word[i]] += 10 ** (len(word) - (i + 1))

# alp를 value값으로 내림차순 정렬해주기
alp = sorted(alp.items(), key=lambda x: -x[1])

# value값이 가장 큰 알파벳부터 9, 8, 7, ... 순으로 배정해서 결과값에 더해주기
answer = 0
for idx, alpha in enumerate(alp):
    answer += alpha[1] * (9 - idx)
print(answer)
