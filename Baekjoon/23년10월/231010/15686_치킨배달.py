from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 치킨집, 집 위치 리스트
chicken, house = [], []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

result = 10**9
visited = []

#########################################
# 백트래킹 사용시


def dfs(cnt, i):      # cnt : 고른 치킨집 수, i : 현재 치킨집 번호
    global result
    dis = 0
    # M개의 치킨집을 골랐을 경우 치킨거리 계산해주기
    if cnt == M:
        # 모든 집으로부터의 치킨거리 계산해야함
        for hx, hy in house:
            # 해당 집으로부터 가장 가까운 치킨집의 거리 tmp
            min_d = 10**9
            # 선택된 치킨집 위치 모두 살펴보기
            for cx, cy in visited:
                tmp = abs(hx - cx) + abs(hy - cy)
                if tmp < min_d:
                    min_d = tmp
            dis += min_d
        # 모든 집을 다 돌아본 후 해당 조합의 치킨거리와 result 비교, 더 작은값으로 result 갱신
        result = min(dis, result)
        return

    # 다음 치킨집 선택해보기
    for idx in range(i, len(chicken)):
        visited.append(chicken[idx])
        dfs(cnt + 1, idx + 1)
        visited.pop()


for i in range(len(chicken)):
    dfs(0, i)
print(result)


#########################################
# itertools 사용 시


# # 치킨집의 조합 구하기
# com = combinations(chicken, M)

# # 선택된 치킨집과 각 집들까지의 거리를 통해 치킨거리 구하는 함수


# def cal(lst):
#     min_d = 0
#     # 집의 좌표
#     for hx, hy in house:
#         tmp = 10**9
#         # 조합에 포함된 치킨집 좌표 cx, cy
#         for cx, cy in lst:
#             tmp = min(tmp, abs(hx - cx) + abs(hy - cy))
#         # 해당 집에서 가장 가까운 치킨집까지의 거리 min_d에 저장해주기
#         min_d += tmp
#     return min_d


# # 조합별로 치킨거리 구해서 가장 작은 값 출력해주기
# result = 10**9
# for chi in com:
#     result = min(result, cal(chi))
# print(result)
