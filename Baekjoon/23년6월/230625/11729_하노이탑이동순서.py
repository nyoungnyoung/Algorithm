import sys

# n - 1개의 원반을 2번으로 모두 옮긴 후 가장 큰 원반을 3번으로 옮기고 나머지들을 3번으로 옮기면 됨


def hanoi(n, start, end):
    # 원반 개수가 1이면 목표 기둥으로 바로 원반 이동 가능
    if n == 1:
        print(start, end)
        return
    # 가장 큰 원반 제외 모든 원반을 보조 기둥(2)으로 옮겨야 함!
    hanoi(n-1, start, 6 - start - end)
    print(start, end)
    # 보조 기둥 -> 목표 기둥으로 원반 이동
    hanoi(n-1, 6 - start - end, end)


N = int(sys.stdin.readline().strip())
print(2 ** N - 1)
hanoi(N, 1, 3)
