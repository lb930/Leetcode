def longest_prefix(strs):
    r = list(zip(*strs))

    prefix = []
    for ele in r:
        if len(set(ele)) == 1:
            prefix.append(ele[0])
        else:
            break
    return ''.join(prefix)