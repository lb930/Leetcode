def balanced_string(s):
    l = r = c = 0
    
    for q in s:
        if q == 'R':
            r += 1
        else:
            l -= 1
        if l + r == 0:
            c += 1
    return c