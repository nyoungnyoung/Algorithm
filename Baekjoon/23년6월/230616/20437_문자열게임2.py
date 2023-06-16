import sys
T = int(sys.stdin.readline().strip())
for tc in range(T):
    W = sys.stdin.readline().strip()
    k = int(sys.stdin.readline().strip())
    # 3, 4번의 개수 세 줄 변수 설정
    cnt_3, cnt_4 = 10000, 0
    # 문자열에 포함되어있는 문자 리스트 만들기
    lst = list(set(W))
    # 리스트 돌아보면서 조건에 맞는 문자열의 길이 저장해주기
    for str in lst:
        # 시작지점
        for i in range(len(W)-k+1):
            # 문자 몇개 포함하는지 확인하기 위한 tmp_k 설정
            tmp_k = k
            # 문자열 길이 임시로 저장할 변수 설정
            tmp_3, tmp_4 = 0, 0
            # 조건에 맞는 문자열은 시작과 끝 문자가 str과 같음!
            if W[i] == str:
                tmp_k -= 1
                tmp_3 += 1
                tmp_4 += 1
                # 종료지점(끝까지 돌아보다가 조건에 맞는 문자열 나오면 문자열 길이 cnt_3/4와 비교해주면 됨)
                for j in range(i+1, len(W)):
                    tmp_3 += 1
                    tmp_4 += 1
                    if W[j] == str:
                        tmp_k -= 1
                        # tmp_k가 0이되면 조건에 맞는 문자열임
                        if not tmp_k:
                            # tmp와 cnt 비교해서 길이 저장해주고 for문 종료
                            if tmp_3 < cnt_3:
                                cnt_3 = tmp_3
                            if tmp_4 > cnt_4:
                                cnt_4 = tmp_4
                            break
    # for문 다 돌고나면 cnt에 조건 만족하는 문자열의 개수 저장되어 있음
    if cnt_3 < 10000 and cnt_4 < 10000:
        print(cnt_3, cnt_4)
    else:
        print(-1)
