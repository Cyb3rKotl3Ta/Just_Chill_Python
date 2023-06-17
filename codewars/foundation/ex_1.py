def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    print([x+(x*i) for i in range(0, n)])
count_by(1, 5)
count_by(2, 5)
count_by(3, 5)
count_by(50, 5)
count_by(100, 5)