import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())
result = 0

# N이 0이 될 때까지 탐색
while N != 0:
    N -= 1
    l = 2 ** N

    # 2사분면
    if r < l and c < l:
        result += 0

    # 1사분면
    elif r < l and c >= l:
        result += l * l
        c -= l

    # 3사분면
    elif r >= l and c < l:
        result += l * l * 2
        r -= l

    # 4사분면
    else:
        result += l * l * 3
        r -= l
        c -= l 


print(result)

