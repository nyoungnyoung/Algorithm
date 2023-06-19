import sys
S = sys.stdin.readline().strip()
sub_s = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        sub_s.add(S[i:j+1])
print(len(sub_s))
