import sys
from collections import defaultdict

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    cloth = defaultdict(int)
    result = 1
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        cloth[b] += 1
    
    for key, value in cloth.items():
        result *= cloth[key] + 1
    
    print(result - 1)