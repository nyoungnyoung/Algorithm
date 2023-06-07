from collections import deque

# 5반올림 시 올림해주는 반올림 함수 새로 만들어주기
def new_round(num):
    return int(num) + 1 if num - int(num) >= 0.5 else int(num)

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
if n == 0:
    print(0)
else:
    out = new_round(n * 0.15)   # 위/아래에서 각각 제외할 사람 수
    lst.sort()                  # 정렬해주기(낮은 수 -> 높은 수)
    lst = deque(lst)            # deque로 바꿔주기
    for i in range(out):
        lst.popleft()
        lst.pop()
    print(new_round(sum(lst) / (n - 2 * out)))


# # 처음 푼 방법
# # 5반올림 시 올림해주는 반올림 함수 새로 만들어주기
# def new_round(num):
#     return int(num) + 1 if num - int(num) >= 0.5 else int(num)

# n = int(input())
# lst = []
# sum_l, result = 0, 0
# for _ in range(n):
#     lst.append(int(input()))
# if lst:
#     out = new_round(n * 0.15)   # 위/아래에서 각각 제외할 사람 수
#     lst.sort()              # 정렬해주기(낮은 수 -> 높은 수)
#     for i in range(out, len(lst)-out):  # 제외할 사람의 의견 빼고 난이도 더해주기
#         sum_l += lst[i]
#     result = new_round(sum_l / (n - (2*out)))
# print(result)    