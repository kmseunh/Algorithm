import sys

n = int(sys.stdin.readline())
word_list = []

for _ in range(n):
    word = sys.stdin.readline()
    word_list.append(word)

word_list = list(set(word_list))
word_list.sort()
word_list.sort(key=lambda x: len(x))

for i in word_list:
    print(i, end="")
