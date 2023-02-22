def solution(today, terms, privacies):
    answer = []
    to_y, to_m, to_d = map(int, today.split('.'))

    termsInfo = {}                       # 약관 정보 담아줄 딕셔너리 만들어주기
    for term in terms:
        term = term.split()
        termsInfo[term[0]] = int(term[1])
    
    for i in range(len(privacies)):
        agree_date, apply = privacies[i].split()
        y, m, d = map(int, agree_date.split('.'))
        m += termsInfo[apply]
        d -= 1
        if m > 12:      # 더해준 만료일자가 12보다 크면 y에 더해줘야함
            y += m // 12
            m = m % 12
        if d == 0:
            m -= 1
            d = 28

    if (to_y * 28 * 12 + to_m * 28 + to_d - (y * 12 * 28 - m * 28 - d)) < 0:
        answer.append(i+1)
        
        # 유효기간 지났는지 판단
        # if y < to_y:
        #     answer.append(i+1)
        # else:
        #     if m < to_m:
        #         answer.append(i+1)
        #     else:
        #         if d < to_d:
        #             answer.append(i+1)
        # print(y, m, d)
        # print("today", to_y, to_m, to_d)
    return answer