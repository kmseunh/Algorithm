n, m = map(int, input().split())
Basket = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    Basket[i-1], Basket[j-1] = Basket[j-1], Basket[i-1]

for i in Basket:
    print(i, end=" ")
