import sys
input = sys.stdin.readline

N = int(input().strip())
score = [int(input().strip()) for _ in range(N)]
# 점수 뒤쪽부터 탐색하면서 이전 점수보다 -1 해주면 됨
cnt = 0
for i in range(N-1, 0, -1):
    if score[i] <= score[i - 1]:
        cnt += score[i - 1] - score[i] + 1
        score[i - 1] = score[i] - 1

print(cnt)
