def isPalindrome(s):
    s = "".join([c if c.isalnum() else "" for c in s])
    return s.lower() == s[::-1].lower()