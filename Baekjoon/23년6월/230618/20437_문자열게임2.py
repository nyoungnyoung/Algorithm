import sys
from collections import defaultdict


def length(dic):
    min_l = 10000
    max_l = 0
    for i in dic:
        for j in range(len(dic[i])-k + 1):
            length = dic[i][j+k-1] - dic[i][j] + 1
            min_l = min(min_l, length)
            max_l = max(max_l, length)
    return(min_l, max_l)


t = int(sys.stdin.readline())
for _ in range(t):
    word = sys.stdin.readline().strip()
    k = int(input())
    dic = defaultdict(list)
    for i in range(len(word)):
        if word.count(word[i]) >= k:
            dic[word[i]].append(i)
    if not dic:
        print(-1)
    else:
        print(*length(dic))

# 1초에서 실패 뜬 코드
# import sys
# from collections import defaultdict
# T = int(sys.stdin.readline().strip())
# for tc in range(T):
#     W = sys.stdin.readline().strip()
#     k = int(sys.stdin.readline().strip())
#     # 문자와 해당 문자의 인덱스 값을 저장해줄 딕셔너리(defaultdict 사용)
#     dic = defaultdict(list)
#     for i in range(len(W)):
#         if W.count(W[i]) >= k:
#             dic[W[i]].append(i)
#     # k개 이상 있는 문자가 하나도 없으면 -1 출력
#     if not dic:
#         print(-1)
#         break

#     # 3, 4번의 개수를 세 줄 변수 설정
#     cnt_3, cnt_4 = 10000, 0

#     # 딕셔너리 돌아보며 3, 4번 조건을 만족하는 글자의 길이 구해주기
#     for idx in dic.values():
#         # idx : 같은 문자의 인덱스 리스트, i : 글자 비교 시작지점
#         for i in range(len(idx) - k + 1):
#             # i ~ i + k번째 인덱스 값의 차이(글자 길이 구해주기)
#             tmp = idx[i+k-1] - idx[i] + 1
#             if tmp < cnt_3:
#                 cnt_3 = tmp
#             if tmp > cnt_4:
#                 cnt_4 = tmp

#     print(cnt_3, cnt_4)

    # 두번째로 푼 방법 -> 아예 풀이 방법이 틀림

    # # 딕셔너리 돌아보며 3, 4번 조건을 만족하는 글자의 길이 구해주기
    # for str in dic:
    #     # value값이 2개 이상일 때만 인덱스 간의 차 확인해보면 됨
    #     if len(dic[str]) > 1:
    #         for i in range(len(dic[str])-1):
    #             for j in range(i+1, i+2):
    #                 tmp_l = abs(dic[str][i] - dic[str][j]) + 1
    #                 if tmp_l > 0:
    #                     if tmp_l < cnt_3:
    #                         cnt_3 = tmp_l
    #                     if tmp_l > cnt_4:
    #                         cnt_4 = tmp_l
    # if cnt_3 < 10000 and cnt_4 > 0:
    #     print(cnt_3, cnt_4)
    # else:
    #     print(-1)

    # 첫번째로 푼 방법 -> 시간초과

    # # 3, 4번의 개수 세 줄 변수 설정
    # cnt_3, cnt_4 = 10000, 0
    # # 문자열에 포함되어있는 문자 리스트 만들기
    # lst = list(set(W))
    # # 리스트 돌아보면서 조건에 맞는 문자열의 길이 저장해주기
    # for str in lst:
    #     # 시작지점
    #     for i in range(len(W)-k+1):
    #         # 문자 몇개 포함하는지 확인하기 위한 tmp_k 설정
    #         tmp_k = k
    #         # 문자열 길이 임시로 저장할 변수 설정
    #         tmp_3, tmp_4 = 0, 0
    #         # 조건에 맞는 문자열은 시작과 끝 문자가 str과 같음!
    #         if W[i] == str:
    #             tmp_k -= 1
    #             tmp_3 += 1
    #             tmp_4 += 1
    #             # 종료지점(끝까지 돌아보다가 조건에 맞는 문자열 나오면 문자열 길이 cnt_3/4와 비교해주면 됨)
    #             for j in range(i+1, len(W)):
    #                 tmp_3 += 1
    #                 tmp_4 += 1
    #                 if W[j] == str:
    #                     tmp_k -= 1
    #                     # tmp_k가 0이되면 조건에 맞는 문자열임
    #                     if not tmp_k:
    #                         # tmp와 cnt 비교해서 길이 저장해주고 for문 종료
    #                         if tmp_3 < cnt_3:
    #                             cnt_3 = tmp_3
    #                         if tmp_4 > cnt_4:
    #                             cnt_4 = tmp_4
    #                         break
    # # for문 다 돌고나면 cnt에 조건 만족하는 문자열의 개수 저장되어 있음
    # if cnt_3 < 10000 and cnt_4 < 10000:
    #     print(cnt_3, cnt_4)
    # else:
    #     print(-1)
