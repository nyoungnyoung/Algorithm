import sys

def star(n):
    if n == 3:
        return ['***', '* *', '***']
    
    # n//3 재귀적으로 실행
    arr = star(n // 3)
    stars = []

    for i in arr:
        stars.append(i * 3)
    
    for i in arr:
        stars.append(i + ' ' * (n//3) + i)
    
    for i in arr:
        stars.append(i * 3)
    
    return stars


N = int(sys.stdin.readline().strip())
print('\n'.join(star(N)))