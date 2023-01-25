numbers = []
for i in range(9):
    j = int(input())
    numbers.append(j)

print(max(numbers))
print(numbers.index(max(numbers))+1)
