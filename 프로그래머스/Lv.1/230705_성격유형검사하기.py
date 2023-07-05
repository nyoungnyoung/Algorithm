def solution(survey, choices):
    answer = ''
    result = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    # survey 길이만큼 돌아보면서 result의 해당 지표에 점수 더해주기
    for i in range(len(survey)):
        a, b = survey[i][0], survey[i][1]
        choice = choices[i]
        # 4보다 작으면 4에서 choice 값 빼준만큼이 점수
        if choice < 4:
            result[a] += 4-choice
        # 4보다 크면 choice에서 4 뺀만큼이 점수
        else:
            result[b] += choice-4
    # result에 결과값 튜플형태로 다시 저장
    result = list(result.items())
    # result의 값들을 2개씩 비교해주기!
    for i in range(0, 8, 2):
        if result[i][1] < result[i+1][1]:
            answer += result[i+1][0]
        else:
            answer += result[i][0]
    return answer