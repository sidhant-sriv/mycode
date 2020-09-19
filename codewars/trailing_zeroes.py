def zeros(n):
    d = 5
    res = 0
    while(n/d>=1):
        res += int(n/d)
        d *= 5
    return res