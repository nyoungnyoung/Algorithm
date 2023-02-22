import sys
words = sys.stdin.readlines()
print(words)
for word in words:
    print(word.rsplit())

# while True:
#     try:
#         print(input())
#     except EOFError:
#         break

