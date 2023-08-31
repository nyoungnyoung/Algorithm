import sys
from collections import defaultdict
input = sys.stdin.readline

p, m = map(int, input().split())
room = defaultdict(list)
num = 0
# {방번호 : [{입장가능한 레벨 목록}, [(플레이어레벨, 닉네임), (플레이어레벨, 닉네임), ...], 남은 정원]}
for _ in range(p):
    l, n = input().split()
    l = int(l)
    # 방이 없으면
    if not room:
        # 새로운 방 생성해주기
        room[num] = [set([i for i in range(l - 10, l + 11)]), {(l, n)}, m - 1]
        num += 1
    # 방이 있으면
    else:
        # 들어갈 방이 있는지 확인해주기
        for i in range(len(room)):
            # room[i][2]가 0이 아니고 room[i][0]에 l이 포함되어 있으면 입장 가능
            if room[i][2] and l in room[i][0]:
                # 입장시키고 남은 정원 - 1
                room[i][1].add((l, n))
                room[i][2] -= 1
                break
        # for문 다 돌아봤는데 break 안걸리면 들어갈 방 없는거
        else:
            # 새로운 방 생성해주기
            room[num] = [
                set([i for i in range(l - 10, l + 11)]), {(l, n)}, m - 1]
            num += 1
            break
print(room)
