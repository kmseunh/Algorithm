n = int(input())
numbers = list(map(int, input().split()))
sosu = 0

for i in numbers:
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                sosu += 1
            break
print(sosu)
