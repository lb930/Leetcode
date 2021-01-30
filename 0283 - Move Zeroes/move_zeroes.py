def zero(nums):
    z = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i != z:
                nums[i], nums[z] = nums[z], nums[i]
            z += 1
    print(nums)