nums = []

for a in range(1,31):
    nums.append(a)

print(nums)

print("----------------------------")
divisible_by_three = [p for p in nums if p % 3 == 0]
print(divisible_by_three)