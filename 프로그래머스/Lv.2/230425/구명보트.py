def solution(people, limit):
    answer = 0
    people.sort()
    max_i, min_i = len(people)-1, 0
    while max_i >= min_i:
        if people[max_i] + people[min_i] <= limit:
            min_i += 1
        max_i -= 1
        answer += 1
    return answer

# # 처음에 푼 방법
# def solution(people, limit):
#     answer = 0
#     people.sort()
#     max_i, min_i = len(people)-1, 0
#     while max_i >= min_i:
#         # 가장 무거운사람 + 가장 가벼운사람 <= limit : 둘다 빼기! 
#         if people[max_i] + people[min_i] <= limit:
#             max_i -= 1
#             min_i += 1
#             answer += 1
#         # 아니면 무거운 사람만 빼주기
#         else:       
#             max_i -= 1
#             answer += 1
#     return answer

solution([70, 50, 80, 50], 100)
solution([70, 80, 50], 100)