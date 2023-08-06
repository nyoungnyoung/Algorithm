import sys
input = sys.stdin.readline

# 두 점 사이의 거리 구하는 함수
def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

Ax, Ay, Bx, By, Cx, Cy = map(int, input().split())
A, B, C = (Ax, Ay), (Bx, By), (Cx, Cy)

# 세 개의 점이 같은 선 위에 있을 경우 평행사변형 만들 수 없음
if (Ax - Bx) * (Ay - Cy) == (Ay - By) * (Ax - Cx):
    print(-1.0)
else:
    # 선의 길이 리스트
    lst = [distance(A, B), distance(B, C), distance(A, C)]
    # 최대 둘레와 최소둘레의 차 : (가장 긴 변 - 가장 짧은 변) * 2
    result = max(lst) - min(lst)
    print(2 * result)