N = int(input())
lst = []
for _ in range(N//4):
    lst.append("long")
lst.append("int")
print(*lst)
