# 입력 받기
words = [list(input()) for _ in range(5)]
# 세로방향으로 읽기
for i in range(15):
    for j in range(5):
        # 단어의 길이보다 i가 작으면 index 내
        if i < len(words[j]):
            # 출력
            print(words[j][i], end='')