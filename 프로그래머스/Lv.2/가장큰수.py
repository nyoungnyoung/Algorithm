# 처음에 푼 방법
# from itertools import permutations

# def solution(numbers):
#     answer = ''
#     for nums in permutations(numbers):
#         num = ''
#         for j in range(len(nums)):
#             num += str(nums[j])
#         if answer < num:
#             answer = num
#     return answer

# 풀이 방법 찾아보니 sort에 key값으로 람다함수 전달하는 방법 사용하면 되나봄!
def solution(numbers):
    nums = list(map(str, numbers))
    # nums.sort(reverse=True)
    nums.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(nums)))
    return answer