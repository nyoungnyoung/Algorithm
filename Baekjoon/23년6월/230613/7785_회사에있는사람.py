# 처음에 input으로 입력받았는데 너무 느려서 sys로 바꿈
import sys

n = int(sys.stdin.readline())
Log = set()
for _ in range(n):
    name, log = sys.stdin.readline().split()
    if log == 'enter':
        Log.add(name)
    else:
        Log.discard(name)
Log = sorted(list(Log), reverse=True)
for i in Log:
    print(i)
