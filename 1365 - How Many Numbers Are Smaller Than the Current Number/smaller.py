def smaller(nums):
    d = {}
    sorted_list = sorted(nums)
    l = len(nums)
    for i in range(l):
        if sorted_list[i] not in d:
            d[sorted_list[i]] = i
    return [d[n] for n in nums]