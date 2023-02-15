def solution(n, words):
    answer, used = [], []
    for i in range(len(words)):
        if words[i] not in used:        # 현재 단어가 used에 없으면 통과
            if i >= 1:                  # 첫순서 제외하고는 끝말잇기 규칙 점검해야함
                if used[-1][-1] == words[i][0]:     # 같으면 통과
                    used.append(words[i])
                else:                   # 다르면 탈락
                    answer = [(i+1) % n, (i + 1) // n + 1]
            else:       # 첫순서면 그냥 used에 추가해주기
                used.append(words[i])
        else:           # used에 있으면 탈락
            answer = [(i+1) % n, (i + 1) // n + 1]
    if not answer:   
        answer = [0, 0] 

    return answer


solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])