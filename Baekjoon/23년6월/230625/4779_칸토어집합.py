import sys


def cantor(start, n):
    # n이 1이 되면(선의 길이가 1이되면) return해주기
    if n == 1:
        return
    # 재귀로 선 잘라주기
    cut = n // 3        # 자른 선의 길이
    # 3등분 한 선들 중 가운데 부분 공백으로 바꿔주기
    for i in range(start + cut, start + cut * 2):
        lines[i] = ' '
    # 왼쪽, 오른쪽 선들은 다시 잘라주기
    cantor(start, cut)
    cantor(start + cut * 2, cut)


while True:
    try:
        N = int(sys.stdin.readline().strip())
        lines = ['-'] * (3 ** N)
        cantor(0, 3 ** N)
        print(''.join(lines))
    except:
        break
