import sys
N = int(sys.stdin.readline())
cnt = 0
for _ in range(N):
    word = sys.stdin.readline().strip()
    visited = set(word[0])
    now = word[0]
    for i in word:
        # now와 i가 다르면
        if i != now:
            # visited에 i가 있는지 확인
            if i in visited:
                break
            # 없으면
            else:
                # now를 i로 변경해주고 visited에 추가
                now = i
                visited.add(now)
    # break에 안걸리고 for문 끝까지 돌았으면
    else:
        cnt += 1
print(cnt)
