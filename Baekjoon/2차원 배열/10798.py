word = [[0]*15 for i in range(15)]

for i in range(5):
    a = list(input())
    a_len = len(a)
    for j in range(a_len):
        word[i][j] = a[j]

for i in range(15):
    for j in range(5):
        if word[j][i] == 0:
            continue
        else:
            print(word[j][i], end="")
