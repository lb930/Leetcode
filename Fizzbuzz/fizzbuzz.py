# Naive approach

def fizzbuzz(num):
    fizz = []
    for n in range(1, num+1):
        if n%3==0 and n%5==0:
            fizz.append('FizzBuzz')
        elif n%3==0:
            fizz.append('Fizz')
        elif n%5==0:
            fizz.append('Buzz')
        else:
            fizz.append(str(n))
    return fizz

# Optimised solution (eg if number is divisible by 7, we want to add 'Jazz', 
# without adding all possible combinations of 'Fizz', 'Buzz', 'Jazz' into an if statement)

def fizzbuzz_2(num):
    fizz = []
    buzz = ''

    for n in range(1, num+1):
        if n%3==0:
            buzz += 'Fizz'
        if n%5==0:
            buzz += 'Buzz'
        if n%7==0:
            buzz += 'Jazz'
        if buzz=='':
            buzz = str(n)
        fizz.append(buzz)
        buzz = ''
    return fizz