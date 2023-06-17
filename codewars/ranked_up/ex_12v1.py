def zero(f = None): return 0 if f is None else int(f(0))
def one(f = None): return 1 if f is None else int(f(1))
def two(f = None): return 2 if f is None else int(f(2))
def three(f = None): return 3 if f is None else int(f(3))
def four(f = None): return 4 if f is None else int(f(4))
def five(f = None): return 5 if f is None else int(f(5))
def six(f = None): return 6 if f is None else int(f(6))
def seven(f = None): return 7 if f is None else int(f(7))
def eight(f = None): return 8 if f is None else int(f(8))
def nine(f = None): return 9 if f is None else int(f(9))

def plus(add): 
    return lambda res: res + add
def minus(sub):
    return lambda res: res - sub
def times(mult): 
    return lambda res: res * mult
def divided_by(div): 
    return lambda res: res / div

print(seven(times(five(plus(four())))))
# print(four(plus(nine())))
# print(eight(minus(three())))
# print(six(divided_by(two())))


