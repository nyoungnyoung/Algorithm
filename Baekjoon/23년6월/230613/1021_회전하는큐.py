import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
queue = deque([i for i in range(1, N+1)])

cnt = 0     # 2, 3번 연산 수행 시 +1
# 뽑아낼 숫자 다 뽑아낼 때까지 연산 수행
for i in lst:
    # 숫자를 뽑을 때까지 반복
    while True:
        # 뽑을 숫자가 0번 인덱스에 있을 경우 popleft
        if i == queue[0]:
            queue.popleft()
            break
        else:
            # 뽑을 숫자의 인덱스가 deque 길이를 반으로 나눈것보다 작거나 같으면
            if queue.index(i) <= len(queue) // 2:
                # 왼쪽회전
                queue.rotate(-1)
                cnt += 1
            else:
                # 오른쪽 회전
                queue.rotate(1)
                cnt += 1

print(cnt)
