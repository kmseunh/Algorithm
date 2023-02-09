n = int(input())
arr = [[0 for _ in range(100)]for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

count = 0
for k in range(100):
    count += arr[k].count(1)

print(count)
