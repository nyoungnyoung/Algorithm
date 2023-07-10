# 이긴사람 판단하기
def win(p, board):
    # 가로줄이 모두 p이면 p가 이긴거
    for i in board:
        if i == [p, p, p]:
            return True
    # 세로줄이 모두 p이면 p가 이긴거
    for j in range(3):
        if [board[i][j] for i in range(3)] == [p, p, p]:
            return True
    # 대각선이 모두 p이면 p가 이긴거
    if [board[0][0], board[1][1], board[2][2]] == [p, p, p]:     # 왼쪽 대각선
        return True
    if [board[2][0], board[1][1], board[0][2]] == [p, p, p]:     # 오른쪽 대각선
        return True
    
    # 위 경우에 모두 안걸리면 이긴거 X
    return False
            

def solution(board):
    board = [list(i) for i in board]
    cnt_o, cnt_x = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                cnt_o += 1
            elif board[i][j] == 'X':
                cnt_x += 1
                
    # o 개수가 x 개수와 같거나, x개수보다 1 많아야 가능! -> 만족하지 못하면 불가능
    if not (cnt_o == cnt_x or cnt_o == cnt_x + 1):
        return 0

    # 둘 중 한명만 승리해야 가능 -> 둘다 승리한 경우는 불가능
    if win('O', board) and win('X', board):
        return 0
    
    # o가 승리할 경우 o개수가 x개수보다 1 많아야 가능 -> 만족하지 않으면 불가능
    if win('O', board) and cnt_o != cnt_x + 1:
        return 0
    
    # x가 승리할 경우 o개수와 x개수가 같아야 가능 -> 만족하지 않으면 불가능
    if win('X', board) and cnt_o != cnt_x:
        return 0
    
    # 위 조건에 걸리지 않으면 가능!
    return 1
    