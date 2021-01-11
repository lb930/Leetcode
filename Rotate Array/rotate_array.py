def rotate(lst, k):

    a = [0] * len(lst)
    for i in range(len(lst)):
        a[(i + k) % len(lst)] = lst[i]
        
    lst[:] = a # [:] all elements
