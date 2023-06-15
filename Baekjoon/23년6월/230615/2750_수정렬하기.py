import sys
lst = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    lst.append(int(sys.stdin.readline().strip()))
lst.sort()
for i in lst:
    print(i)

# 버블정렬 O(n^2) : 가장 큰값을 맨 뒤에 넣으면서 정렬
def bubble_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# 버블정렬 최적화
def bubble_sort_re(lst):
    for i in range(len(lst) - 1, 0, -1):
        # 이전에 자리 change가 한번도 일어나지 않았다면 sort 종료해도 됨
        flag = False
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                falg = True
        if not flag:
            break

# 선택정렬 O(n^2)
def select_sort(lst):
    for i in range(len(lst) - 1):
        min_i = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_i]:
                min_i = j
        lst[i], lst[min_i] = lst[min_i], lst[i]
