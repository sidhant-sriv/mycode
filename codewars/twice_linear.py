from collections import deque as dq
def dbl_linear(n):
    h = 1
    cnt = 0
    a, b = dq([]), dq([])
    while True:
        if (cnt >= n):
            return h
        a.append(2 * h + 1)
        b.append(3 * h + 1)
        
        h = min(a[0], b[0])
        if h == a[0]: 
            h = a.popleft()
        if h == b[0]:
            h = b.popleft()
        cnt += 1