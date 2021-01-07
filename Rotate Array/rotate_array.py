def rotate(lst, k):

    a = [0] * len(lst)
    for i in range(len(lst)):
        a[(i + k) % len(lst)] = lst[i]
        
    lst[:] = a # [:] all elements
    print(lst)

rotate([1, 2, 3, 4, 5, 6, 7], 3)