from itertools import product
import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
num = [i for i in range(1, N + 1)]
lst = list(product(num, repeat=M))
for i in lst:
    print(*i)