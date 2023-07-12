def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    win = 0
    cnt_0 = 0
    
    # in 연산 속도 높혀주기 위해 set으로 변경해주기
    win_nums = set(win_nums)
    # 0 개수 세주기
    cnt_0 = lottos.count(0)
    # lottos에 있는 번호들 돌아보면서 win_nums에 있는지 확인해주면 됨
    for lotto in lottos:
        # 번호가 당첨 번호이면 win + 1
        if lotto in win_nums:
            win += 1

    # 당첨 가능한 최고 개수는 cnt_0과 win을 합친 개수
    return [rank[cnt_0 + win], rank[win]]