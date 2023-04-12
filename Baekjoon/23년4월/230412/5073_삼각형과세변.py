import sys
while True:
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort(reverse=True)
    if lst[0] == lst[1] == lst[2] == 0:
        break
    elif lst[0] >= lst[1] + lst[2]:
        print("Invalid")
    elif lst[0] == lst[1] == lst[2]:
        print("Equilateral")
    elif lst[0] != lst[1] != lst[2]:
        print("Scalene")
    else:
        print("Isosceles")