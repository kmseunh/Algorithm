arr = []

for _ in range(9):
    arr.append(list(map(int, input().split())))

x = 0
y = 0
max_num = -1
for raw in range(9):
    for col in range(9):
        if arr[raw][col] > max_num:
            x = raw + 1
            y = col + 1
            max_num = arr[raw][col]
print(max_num)
print(x, y)
