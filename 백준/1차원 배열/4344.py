c = int(input())

for i in range(c):
    test_case = list(map(int, input().split()))
    c = 0
    for j in test_case[1:]:
        avg = sum(test_case[1:])/test_case[0]
        if j > avg:
            c += 1
    rate = c/test_case[0]*100
    print(f'{rate:0.3f}%')
