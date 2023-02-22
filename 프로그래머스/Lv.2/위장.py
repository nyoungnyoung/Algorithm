def solution(clothes):
    answer = 1
    cloth = {}
    for i in clothes:
        key, value = i[1], i[0]
        if key not in cloth:
            cloth[key] = 1
        else:
            cloth[key] += 1

    for i in len(cloth.values()):
        answer *= (i+1)
    return answer - 1

