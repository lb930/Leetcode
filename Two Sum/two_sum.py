def two_sum_dict(nums, target):
    new_dict = {}
    for i, num in enumerate(nums):
        comp = target - num
        if num in new_dict:
            return new_dict[num], i 
        new_dict[comp] = i   

print(two_sum_dict([3, 2, 4], 6))

# Alternative
def two_sum(nums, target):
    new_list = []
    for i in range(len(nums)):
        num = target - nums[i]
        if nums[i] in new_list:
            return nums.index(num), i
        new_list.append(num)

print(two_sum([3, 2, 4], 6))