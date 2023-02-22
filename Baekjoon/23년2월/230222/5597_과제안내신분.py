lst = [int(input()) for _ in range(28)]
for i in range(1, 31):
    if i not in lst:
        print(i)


# 다른사람 풀이
# print(*{*map(int, open(0))}^{*range(1,31)})