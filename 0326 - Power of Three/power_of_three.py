# Recursive (slow)

def three(num):
    if num == 1:
        return True
    elif num < 3:
        return False
    else:
        return three(num/3)

# while loop (medium fast)

def three2(num):
    if num == 0:
        return False
    while num % 3 == 0:
        num /=3
    if num == 1:
        return True
    return False

# take advantage of highest limitation is 3**19 = 1162261467 since Integer has range <2147483648, 
# so if 1162261467 % n == 0, then True

def three3(num):
    lst = [3**n for n in range(20)]
    if num in lst:
        return True