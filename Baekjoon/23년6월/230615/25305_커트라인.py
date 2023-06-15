import sys

N, k = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))
# 내림차순으로 정렬후 상을 받는 k명 중 가장 점수가 낮은 사람의 점수(k-1번째 수) 출력
score.sort(reverse=True)
print(score[k-1])
