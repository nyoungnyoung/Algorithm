import sys
input = sys.stdin.readline

word1, word2 = input().strip(), input().strip()
l1, l2 = len(word1), len(word2)
dp = [0] * l2

# word1과 word2를 돌아보면서 글자 하나씩 비교
for i in range(l1):
    cnt = 0
    for j in range(l2):
        # 글자가 다른 경우 cnt가 dp[j]보다 작을 때 교체(최댓값 저장을 위해)
        if cnt < dp[j]:
            cnt = dp[j]
        # 같은 글자면 cnt에 + 1 더한 값 dp에 저장
        elif word1[i] == word2[j]:
            dp[j] = cnt + 1
# dp 리스트에서 가장 큰 값 출력
print(max(dp))