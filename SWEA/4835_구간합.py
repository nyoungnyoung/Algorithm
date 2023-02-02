T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    max_num, min_num = 0, float('inf')      # max/min에 임의의 수 할당
    for i in range(N-M+1):                  # 반복문 끝나는 지점 정하기
        sum_num = 0                         # i부터 M개 누적합 구해줄 임시변수 설정
        for j in range(i, i+M):             # i부터 M개!
            sum_num += lst[j]       
        if max_num < sum_num:               # 현재 누적합과 max/min값 비교해서 저장
            max_num = sum_num
        if min_num > sum_num:
            min_num = sum_num
    print(f'#{tc} {max_num-min_num}')