import sys
input = sys.stdin.readline

N = int(input().strip())
lst = [int(input().strip()) for _ in range(N)]

# lst를 정렬한 뒤 선택된 로프 중 들 수 있는 무게가 가장 작은 로프의 무게 * 로프 수 구해주기
lst.sort()
result = []
for w in lst:
    result.append(w * N)
    N -= 1
print(max(result))