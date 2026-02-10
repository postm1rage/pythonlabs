number = (input())

nums = []
for n in number:
    nums.append(n)

nums = [int(n) for n in nums]
nums = sorted(nums)

if ((nums[0] + nums[2]) / 2 == nums[1]):
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")