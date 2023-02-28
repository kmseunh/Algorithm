n = int(input())

for i in range(n):
    test_case = list(map(int, input().split()))
    cnt = 0
    for j in test_case[1:]:
        avg = sum(test_case[1:])/test_case[0]
        if j > avg:
            cnt += 1
    rate = cnt/test_case[0]*100
    print(f'{rate:0.3f}%')
