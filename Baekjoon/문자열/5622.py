numbers = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for i in range(len(numbers)):
    for j in dial:
        if numbers[i] in j:
            time += dial.index(j) + 3

print(time)
