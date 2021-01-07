def two_sum_2(lst, target):
    l, r = 0, len(lst)-1

    while l < r:
        comp = lst[l] + lst[r]
        if comp == target:
            return l+1, r+1
        elif comp < target:
            l += 1
        else:
            r -= 1

print(two_sum_2([-1, 0], -1))