a, b = input().split()
r_a = a[::-1]
r_b = b[::-1]

if int(r_a) > int(r_b):
    print(r_a)
else:
    print(r_b)
