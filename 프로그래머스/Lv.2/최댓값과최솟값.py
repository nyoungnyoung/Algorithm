def solution(s):
    word = sorted(list(map(int, s.split())))
    answer = f'{word[0]} {word[-1]}'
    return answer


solution("-1 -2 -3 -4")
