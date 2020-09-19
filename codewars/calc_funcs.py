import math
def zero(p = None): return 0 if not p else p(0)
def one(p = None): return 1 if not p else p(1)
def two(p = None): return 2 if not p else p(2)
def three(p = None): return 3 if not p else p(3)
def four(p = None): return 4 if not p else p(4)
def five(p = None): return 5 if not p else p(5)
def six(p = None): return 6 if not p else p(6)
def seven(p = None): return 7 if not p else p(7)
def eight(p = None): return 8 if not p else p(8)
def nine(p = None): return 9  if not p else p(9)

def plus(n): return lambda x: x+n  
def minus(n): return lambda x: x-n
def times(n): return lambda x: x*n 
def divided_by(n): return lambda x:math.floor(x/n )
#three(plus(five())) = 8