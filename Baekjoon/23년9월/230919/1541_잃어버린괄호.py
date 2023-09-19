import sys

input = sys.stdin.readline

# - 부호를 기준으로 식 입력받기
exp = input().strip().split("-")

# - 부호로 나눈 식들의 결과 계산해서 lst에 저장해주기
lst = []

for str in exp:
    # str 식의 결과를 계산해서 lst에 추가해주기
    tmp = map(int, str.split("+"))
    num = sum(tmp)
    lst.append(num)

# lst 돌아보면서 첫번째 값에서 나머지 값들 차례대로 빼주기
for i in range(len(lst)):
    if i == 0:
        result = lst[i]
    else:
        result -= lst[i]

print(result)