def missing_number(nums):
    n = len(nums)
    # Gauss's law
    return int(n * (n+1) / 2 - sum(nums))