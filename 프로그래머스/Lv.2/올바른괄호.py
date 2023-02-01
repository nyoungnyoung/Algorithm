def solution(s):
    answer = True
    stack = []
    # 문자열을 돌면서 stack에 넣어주기
    for i in s:
        if i == '(':        # i가 '('일 때 : stack에 넣기
            stack.append(i)
        else:               # i가 ')'일 때
            if stack:       # stack이 비어있지 않으면 '('제거
                stack.pop()
            else:           # stack이 비어있으면 flase
                answer = False
    if stack:               # for문 다 돌았는데 stack이 비어있지 않으면 false
        answer = False
    return answer