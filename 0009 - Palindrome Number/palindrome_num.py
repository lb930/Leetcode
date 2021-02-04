def is_palindrome(x):
    if x < 0:
        return False
    else:
        new = 0
        check = x
        while x != 0:
            new = (new * 10) + x % 10
            x = x // 10
        if new == check:
            return True