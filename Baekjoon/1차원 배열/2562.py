numbers = []
for i in range(9):
    j = int(input())
    numbers.append(j)

print(max(numbers))
## 출력하기
print(numbers.index(max(numbers))+1)
