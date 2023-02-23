word = input()
newWord = ''
for i in word:
    if i.isupper():
        newWord += i.lower()
    else:
        newWord += i.upper()
print(newWord)