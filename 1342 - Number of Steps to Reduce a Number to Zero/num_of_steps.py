def numberOfSteps(num):
    step_counter = 0

    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        step_counter +=1
        
    return step_counter