def solution(nums):
    answer = 0
    lst = list(set(nums))
    n = len(nums) // 2
    if len(lst) > n:
        answer = len(lst)
    else:
        answer = n
    return answer