def solution(record):
    answer = []
    userDB, visit = {}, []               # user정보 기록해줄 딕셔너리, 기록 남겨줄 리스트 생성
    for info in record:
        chat = info.split()
        work, uid = chat[0], chat[1]
        if work in ('Enter', 'Change'):  # enter나 change면
            userDB[uid] = chat[2]        # user정보에 id와 닉네임 기록
            visit.append((uid, work))    # 방문기록에 id와 처리한 작업 기록
        else:                            # leave면
            visit.append((uid, work))    # 방문기록에 id와 처리한 작업만 기록
    
    # 방문기록 살펴보면서 '닉네임'님이 들어왔습니다 출력해주기!
    for log in visit:
        if log[1] == 'Enter':
            answer.append(f'{userDB[log[0]]}님이 들어왔습니다.')
        elif log[1] == 'Leave':
            answer.append(f'{userDB[log[0]]}님이 나갔습니다.')

    return answer