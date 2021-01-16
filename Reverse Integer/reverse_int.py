def reverse_int(num):  
  
    # Handling negative numbers  
    negative_flag = False
    if num < 0: 
        negative_flag = True
        num = -num  

    rev_num = 0

    while num != 0:  
      
        # isolate the last digit of an integer
        curr_digit = num % 10

        # append current_digit to rev_num
        rev_num = (rev_num * 10) + curr_digit
        print(rev_num)  
  
        # check overflow
        if rev_num >= 2147483647 or -rev_num <= -2147483648:
            return 0 
        
        # removes the last digit from the number so we can iterate through the whole integer and take the next digit
        # eg 19/10 = 1.9; floor(1.9) = 1
        num = num // 10

    return -rev_num if (negative_flag == True) else rev_num
