n = int(input())
hansu = 0

for i in range(1, n+1):
    nums = list(map(int, str(i)))
    if i <= 99:
        hansu += 1
    elif nums[0] - nums[1] == nums[1] - nums[2]:
        hansu += 1
        
print(hansu)
