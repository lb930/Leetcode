def majority_element(nums):
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
        if d[num] > len(nums) / 2:
            return num