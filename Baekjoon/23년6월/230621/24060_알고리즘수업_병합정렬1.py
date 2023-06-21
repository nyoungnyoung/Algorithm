# 다시 풀어보기..!!

import sys


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = (len(arr) + 1) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = r = 0
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            merged_arr.append(left_arr[l])
            l += 1
        else:
            merged_arr.append(right_arr[r])

    merged_arr += left_arr[l:]
    merged_arr += right_arr[r:]

    return merged_arr


N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
result = merge_sort(A)

if len(result) >= K:
    print(result[K-1])
else:
    print(-1)


# 다른사람 코드
# import sys
# input = sys.stdin.readline


# def mergeSort(L):
#     if len(L) == 1:
#         return L

#     mid = (len(L) + 1)//2
#     left = mergeSort(L[:mid])
#     right = mergeSort(L[mid:])

#     L2 = []
#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             L2.append(left[i])
#             ans.append(left[i])
#             i += 1
#         else:
#             L2.append(right[j])
#             ans.append(right[j])
#             j += 1

#     while i < len(left):
#         L2.append(left[i])
#         ans.append(left[i])
#         i += 1

#     while j < len(right):
#         L2.append(right[j])
#         ans.append(right[j])
#         j += 1

#     return L2

# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# ans = []
# mergeSort(a)

# if len(ans) >= k:
#     print(ans[k-1])
# else:
#     print(-1)
