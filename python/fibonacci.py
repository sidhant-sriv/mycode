from functools import lru_cache
import math
@lru_cache(maxsize = 512)
def fibonacci(n):
    if n==2 or n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
