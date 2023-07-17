N = int(input())

line, idx = 0, 0
while N > idx:
    line += 1
    idx += line

diff = idx - N
if not line % 2:
    s = line - diff
    m = diff + 1
else:
    s = diff + 1
    m = line - diff

print(f'{s}/{m}')  