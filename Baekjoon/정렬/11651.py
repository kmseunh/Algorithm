import sys

n = int(sys.stdin.readline())
list = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    list.append((x, y))
list.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(list[i][0], list[i][1])
