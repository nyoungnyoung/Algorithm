import sys
input = sys.stdin.readline

R, S = map(int, input().split())
photo = [list(input().strip()) for _ in range(R)]

# 가장 짧은 세로 길이 저장해 줄 변수 min_c
min_c = 10**6

# photo를 세로 우선 탐색
for j in range(S):
    # 세로줄 정보 col, 유성과 땅의 거리 저장해줄 변수 cnt
    col, cnt = "", 0
    for i in range(R):
        # 현재 위치에 있는거 col에 추가해주기
        now = photo[i][j]
        col += photo[i][j]
        # 현재 위치가 땅이면
        if now == "#":
            # 위에 유성이 있는 경우에
            if "X" in col:
                # 마지막 유성과 땅의 거리(공기 개수) cnt에 저장하고 break
                cnt = i - col.rfind("X") - 1
                break
    # cnt가 0이 아니고, 가장 짧은 거리면 min_c 업데이트
    if cnt and cnt < min_c:
        min_c = cnt

result = photo.copy()
# min_c만큼 아래로 떨어뜨려주면됨(아래에서부터 위로 탐색하면서 min_c만큼 . 지워주기)
for j in range(S):
    for i in range(R-1, -1, -1):
        if i + min_c < R:
            # photo[i][j]가 X고 photo[i+min_c][j]가 .이면 둘이 자리 바꿔주면 됨!
            if photo[i][j] == "X" and photo[i + min_c][j] == ".":
                result[i][j], result[i + min_c][j] = photo[i + min_c][j], photo[i][j]

for i in range(R):
    sys.stdout.write("".join(result[i])+'\n')
