word = input()
result = 1
# 단어의 길이 // 2까지 인덱스 돌면서 앞뒤 확인해주기
for i in range(len(word)//2):
    if word[i] != word[-i-1]:
        result = 0
        break
print(result)
