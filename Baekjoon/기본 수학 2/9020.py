def sosu(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True


for _ in range(int(input())):
    t = int(input())

    a, b = t//2, t//2
    while a > 0:
        if sosu(a) and sosu(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
