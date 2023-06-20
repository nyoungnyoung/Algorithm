import sys


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1, 0)


def recursion(s, l, r, cnt):
    cnt += 1
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    else:
        return recursion(s, l+1, r-1, cnt)


T = int(sys.stdin.readline())
for _ in range(T):
    S = sys.stdin.readline().strip()
    print(*isPalindrome(S))
