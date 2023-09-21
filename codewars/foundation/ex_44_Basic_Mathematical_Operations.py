import operator as op

def basic_op(operator, value1, value2):
    ops = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
    return ops[operator](value1, value2)
    
def basic_op_v2(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')


print(basic_op('+', 4, 7))
