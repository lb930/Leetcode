def rotate(lst, k):
    n = len(lst)
    a = [0] * n
    for i in range(n):
        a[(i + k) % n] = lst[i]
        
    lst[:] = a # [:] all elements