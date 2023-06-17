arr = []
def reverse_seq(n):
    arr.append(n)
    if n == 1:
        return arr
    return reverse_seq(n-1)

def reverse_seq2(n):
    return list(range(n,0,-1))

print(reverse_seq(5))
print(reverse_seq2(5))
