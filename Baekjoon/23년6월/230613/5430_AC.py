import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    # 배열에 들어있는 수들 큐에 담아주기(앞뒤의 대괄호 제외, ","로 split)
    queue = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    # 빈배열을 입력받았을 때에도 deque에 ''가 들어감 -> 빈배열로 초기화
    if n == 0:
        queue = deque()

    # reverse는 R이 홀수번 나왔을 때 한번만 해주기 위해서 flag 추가
    flag = 0

    # 연산 시작
    for i in p:
        # R이면 flag +=1
        if i == 'R':
            flag += 1
        elif i == 'D':
            # 배열이 비어있지 않으면 숫자 뽑아주기(마지막에 reverse를 해줘야하므로 pop/popleft 구분필요)
            if queue:
                # flag가 홀수면 오른쪽에서 뽑아주기(reverse 되므로)
                if flag % 2:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                print('error')
                break
    # 연산이 끝난 후 배열이 비어있지 않으면 배열의 내용 출력
    else:
        if flag % 2:
            queue.reverse()
        print(f'[{",".join(queue)}]')
