# Recursive, slowest solution

def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-2) + fib1(n-1)

def fib2(n):
    a = 0
    b = 1

    if n == 0:
        return a 
    if n == 1:
        return b

    n -= 2

    while n >= 0:
        print(n, a, b)
        a, b = b, a + b
        n -= 1
        print(n, a, b)
    return b