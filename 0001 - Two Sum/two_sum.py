def two_sum_dict(nums, target):
    new_dict = {}
    for i, num in enumerate(nums):
        comp = target - num
        if num in new_dict:
            return new_dict[num], i 
        new_dict[comp] = i 
