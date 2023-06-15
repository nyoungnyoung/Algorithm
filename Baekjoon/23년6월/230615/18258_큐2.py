import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    cmd = sys.stdin.readline().strip()
    # push일 때
    if ' ' in cmd:
        num = int(cmd.split()[1])
        queue.append(num)
    # 그 외의 것들
    else:
        if cmd == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif cmd == 'size':
            print(len(queue))
        elif cmd == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif cmd == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif cmd == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)
