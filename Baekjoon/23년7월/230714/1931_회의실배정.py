import sys
N = int(sys.stdin.readline())
# 더 빨리 끝나는 순서대로 정렬, 같으면 더 빨리 시작하는 순서대로 정렬
time = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
# s, e 시간 돌아보면서 마지막 회의 끝나는 시간보다 시작하는 시간이 더 늦거나 같으면 cnt + 1, e를 마지막 회의 끝나는 시간 end로 갱신
end, cnt = 0, 0
for s, e in time:
    if s >= end:
        cnt += 1
        end = e

print(cnt)