def first_unique_char(s):
    if len(s) == 1:
        return 0
    checked = []
    for i in range(len(s)):
        if s[i] not in checked and s[i] in s[i+1:]:
            checked.append(s[i])
        elif s[i] not in checked:
            return i
        elif s[i] not in checked and s[i] not in s[i+1]:
            return i
    return -1