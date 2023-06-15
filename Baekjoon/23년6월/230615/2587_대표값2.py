sum_n = 0
lst = []
for _ in range(5):
    num = int(input())
    sum_n += num
    lst.append(num)
lst.sort()
print(sum_n // len(lst))
print(lst[2])
