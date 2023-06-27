import sys
N, M, B = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = sys.maxsize
height = 0

# 가능한 모든 높이 탐색
for target in range(257):
    take, use = 0, 0

    for i in range(N):
        for j in range(M):
            # 높이가 목표보다 높으면 블록 가져오기
            if graph[i][j] > target:
                take += graph[i][j] - target
            # 높이가 목표보다 낮으면 블록 쓰기
            else:
                use += target - graph[i][j]
    # 내가 가져온 블록보다 사용한 블록이 적어야 가능!
    if take + B >= use:
        time = take * 2 + use
        # 걸리는 시간 비교해서 답 구해주기
        if time <= result:
            result = time
            height = target

print(result, height)