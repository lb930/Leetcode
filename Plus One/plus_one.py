def plus_one(digits):
    length = len(digits) - 1

    while digits[length] == 9: # (last) index equals 9
        digits[length] = 0
        length -= 1
    if length < 0:
        digits = [1] + digits
    else: # length > 0
        digits[length] += 1
    return digits
