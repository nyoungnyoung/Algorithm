tel = {3: ['A', 'B', 'C'], 4: ['D', 'E', 'F'], 5: ['G', 'H', 'I'], 6: ['J', 'K', 'L'], 7: [
    'M', 'N', 'O'], 8: ['P', 'Q', 'R', 'S'], 9: ['T', 'U', 'V'], 10: ['W', 'X', 'Y', 'Z']}
word = input()
cnt = 0
for s in word:
    for num in tel:
        if s in tel[num]:
            cnt += num
            break
print(cnt)
