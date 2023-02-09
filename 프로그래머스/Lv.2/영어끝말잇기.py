def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            answer = [(i % n) + 1, (i // n) + 1]
    return answer

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])