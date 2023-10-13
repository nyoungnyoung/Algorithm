import sys
input = sys.stdin.readline

N = int(input().strip())
lst = [0] * N       # lst[i] = j : 퀸을 [i, j] 위치에 놓는다
answer = 0



# x행에 퀸을 놓는 함수
def n_queen(x):
    global answer
    # N행까지 퀸을 놓았다면 
    if x == N:
        answer += 1
        return
    # 0부터 N열까지 반복문을 돌며 퀸을 놓아본다
    for i in range(N):
        # (x, i)에 퀸을 놓는다
        lst[x] = i
        # 놓을 수 있는 곳이면 다음 행
        if is_valid(x):
            n_queen(x + 1)


# 현재 자리에 퀸을 놓아도 되는지 확인하는 함수
def is_valid(x):
    # x행까지 반복문 돌면서
    for i in range(x):
        # 1. 같은 열에 다른 퀸이 있거나
        if lst[i] == lst[x]:
            return False
        # 2. 왼쪽/오른쪽 대각선에 다른 퀸이 있을 때 퀸을 놓지 못함
        if abs(x - i) == abs(lst[x] - lst[i]):
            return False
    # if문 안걸리면 가능
    return True

n_queen(0)
print(answer)