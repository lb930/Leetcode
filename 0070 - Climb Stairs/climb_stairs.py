def climb_stairs(n):
    a = 0
    b = 1
    n += 1

    if n == 0:
        return a
    elif n == 1:
        return b

    n -= 2
    while n >= 0:
        a, b = b, a + b
        n -= 1
    return b