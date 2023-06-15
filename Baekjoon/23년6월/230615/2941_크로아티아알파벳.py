lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in lst:
    word = word.replace(i, '1')
print(len(word))
