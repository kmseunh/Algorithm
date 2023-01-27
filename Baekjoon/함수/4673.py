numbers = set(range(1, 10001))
new_numbers = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    new_numbers.add(i)

self_num = sorted(numbers - new_numbers)
for i in self_num:
    print(i)
