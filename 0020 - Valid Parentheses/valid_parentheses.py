def valid_p(s):
    stack = []
    d = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in d.values():
            stack.append(char)
        elif stack and stack[-1] == d[char]:
            stack.pop()
        else:
            return False
    return len(stack) == 0