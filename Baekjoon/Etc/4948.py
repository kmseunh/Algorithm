def sosu(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True


all_list = list(range(2, 123456*2))
save_list = []

for i in all_list:
    if sosu(i):
        save_list.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in save_list:
        if n < i <= n*2:
            count += 1
    print(count)
