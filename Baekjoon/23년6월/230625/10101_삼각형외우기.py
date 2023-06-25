sum_n = 0
tri = set()
for _ in range(3):
    A = int(input())
    sum_n += A
    tri.add(A)
if sum_n != 180:
    print("Error")
else:
    if len(tri) == 1:
        print("Equilateral")
    elif len(tri) == 2:
        print("Isosceles")
    else:
        print("Scalene")
