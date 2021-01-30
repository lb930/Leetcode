from string import ascii_letters
import re

def atoi(s):
    s = s.strip()
    s = re.findall('^[+\-]?\d+', s)

    try:
        res = int(''.join(s))
        MAX = 2147483647
        MIN = -2147483648
        if res > MAX:
            return MAX
        if res < MIN: 
            return MIN
        return res
    except: 
        return 0

print(atoi('-3'))

