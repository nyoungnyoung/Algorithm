import sys
N = int(sys.stdin.readline())
lst = list(map(int, input().split()))
# lst에서 중복 제거한 리스트를 오름차순으로 정렬할 경우 각 값의 인덱스가 해당 값보다 큰 수의 개수가 됨
lst_zip = sorted(list(set(lst)))
# dict로 시간복잡도 줄여주기
dict = {lst_zip[i]: i for i in range(len(lst_zip))}
# lst 돌면서 dict[i]값 출력해주기
for i in lst:
    print(dict[i], end=' ')

# print(*lst_zip)

# 시간초과
# for i in range(len(lst)):
#     visited = []
#     for j in range(len(lst)):
#         if i != j and lst[i] > lst[j] and lst[j] not in visited:
#             lst_zip[i] += 1
#             visited.append(lst[j])
