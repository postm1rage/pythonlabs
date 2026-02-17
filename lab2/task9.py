nums = list(map(int, input().split()))

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        print(nums[i])