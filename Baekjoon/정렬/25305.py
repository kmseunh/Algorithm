n, k = map(int, input().split())
score = list(map(int, input().split()))

price = []
for i in range(k):
    price.append(max(score))
    score.remove(max(score))

print(price[-1])
