n = int(input())
arr = []

for _ in range(n):
    number = int(input())
    arr.append(number)
    arr.sort()

for j in range(len(arr)):
    print(arr[j])
