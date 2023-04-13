from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    # 일단 무지성으로 반복하자
    while progresses:
        cnt = 0
        # 진도 증가시키기
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        # progresses가 아직 남아있고, 첫번째 값이 100 이상이면
        while progresses and progresses[0] >= 100:
            cnt += 1                # 배포되는 작업 수 +1  
            progresses.popleft()    # 첫번째 작업 빼주기
            speeds.popleft()        # 첫번째 작업 속도 빼주기
        if cnt:     # cnt가 0보다 크면 answer에 추가해주기
            answer.append(cnt)
    return answer
