from collections import deque

def solution(board, moves):
    cnt = 0
    basket = deque()
    # moves 배열 돌면서 인형뽑기 시작
    for move in moves:
        # move - 1번 위치에서 인형 뽑기 위해 세로축부터 탐색
        for j in range(len(board)):
            # 해당하는 세로축 아니면 넘어가기
            if move - 1 != j:
                continue
            for i in range(len(board)):
                # move - 1과 같은 세로축의 가장 위에 있는 인형을
                if move - 1 == j and board[i][j]:
                    # 뽑아서 바구니에 넣어주기
                    basket.append(board[i][j])
                    board[i][j] = 0
                    break
        # 바구니에 인형 2개 이상 들어가 있을 경우 마지막 두개가 같은 인형인지 확인 후 터뜨리기
        if len(basket) >= 2 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            cnt += 2
    return cnt

result = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(result)