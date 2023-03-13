n = int(input())
list = []

for i in str(n):
    list.append(int(i))
    list.sort(reverse=True)

for j in list:
    print(j, end="")
