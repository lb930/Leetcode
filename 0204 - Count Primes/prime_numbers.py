def count_primes(n) :
    # No prime number less than 2
    if n < 3: 
        return 0     
    
    lst = [1] * n          # create a list for marking numbers less than n
    lst[0] = lst[1] = 0    # 0 and 1 are not prime numbers | 0 marks invalid numbers

    m = 2
    # we only check a number (m) if its square is less than n
    while m * m < n: #        
        if lst[m] == 1:    ###// if m is already marked by 0, no need to check its multiples.
        
            # Sieve of Eratosthenes: all numbers which are multiples of current number (eg 9 is a multiple of 3) are set to 0
            # If m is marked by 1, we mark all its multiples from m * m to n by 0. 
            
            print(f'm:{m}')
            print(f'lst before: {lst}')

            # m*m: square of the current number (starting at 2*2 to rule out even numbers in first iteration)
            # n: range to be checked
            # m: steps (aka multiples of the current number to be checked)

            # 1 + (n - m * m - 1) // m is equal to the number of multiples of m from m * m to n 
            # eg if n=12 and m = 2: (1+(12-2*2-1)//2) = 4 ---> and we want to replace 4 zeroes
            # lst[m * m: n: m] = [0] *(1 + (n - m * m - 1) // m)

            # Slower, but easier to understand
            for i in range(m * m, n,  m):
               lst[i] = 0
            print(f'lst after : {lst}')

        # If it is the first iteration (e.g. m = 2), add 1 to m (e.g. m = m + 1; 
        # which means m will be 3 in the next iteration), 
        # otherwise: (m = m + 2); This way we avoid checking even numbers again.	
        if m == 2:
            m += 1 
        else:
            m += 2
    return sum(lst)