tri = sorted(map(int, input().split()))
# 삼각형의 조건 : 작은 두 변의 길이의 합이 제일 긴 변의 길이보다 커야 함
if tri[0] + tri[1] > tri[2]:
    print(sum(tri))
else:
    print((tri[0] + tri[1]) * 2 - 1)
