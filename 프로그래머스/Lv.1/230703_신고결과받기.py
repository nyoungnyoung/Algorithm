from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)        # 중복신고 제거하기
    cnt = defaultdict(int)      # 신고당한횟수
    accuse = defaultdict(list)  # 신고 목록
    for info in report:
        a, b = info.split()     # a : 신고자 / b : 신고당한사람
        cnt[b] += 1
        accuse[a] += [b]
    # print('신고당한 횟수',cnt)
    # print('신고목록',accuse)
    for user1 in cnt:
        if cnt[user1] >= k:
            for user2 in accuse:
                if user1 in accuse[user2]:
                    answer[id_list.index(user2)] += 1
    return answer
