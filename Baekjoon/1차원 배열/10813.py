n, m = map(int, input().split())
Basket = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    temp = Basket[i]
    Basket[i] = Basket[j]
    Basket[j] = temp

for i in range(1, n+1):
    print(Basket[i], end=" ")
