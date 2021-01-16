def single_num(nums):
    check = {}
    for num in nums:
        check[num] = check.get(num, 0)+1
    for k, v in check.items():
        if v == 1:
            return k