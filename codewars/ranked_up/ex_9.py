def prime_factors(n):
    lst1 = []
    lst2 = []
    i = 2
    while i < 999999999999997:
        if n / i == 1:    
            lst1.append(i)
            for j in set(lst1):
                if lst1.count(j) > 1:
                     lst2.append(f'({j}**{lst1.count(j)})') 
                else: lst2.append(f'({j})')

            return "".join(lst2)
        elif n % i == 0:
            n = n/i
            lst1.append(i)
        else: i+=1
        
    
def prime_factors2(n):
    i = 2
    factors = []
    lst = []
    while i * i <= n+1:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    factors = sorted(factors)
    for j in list(set(factors)):
        if factors.count(j) > 1:
                lst.append(f'({j}**{factors.count(j)})') 
        else: lst.append(f'({j})')
    return ''.join(lst)

def prime_factors3(n):
    while i * i < n:
        while n%i == 0:
            n = n / i
        i = i + 1

def primeFactors4(n):
  result = ''
  fac = 2
  while fac <= n:
    count = 0
    while n % fac == 0:
      n /= fac
      count += 1
    if count:
      result += '(%d%s)' % (fac, '**%d' % count if count > 1 else '')
    fac += 1
  return result

def primeFactors5(n):
    i, j, p = 2, 0, []
    while n > 1:
        while n % i == 0: n, j = n / i, j + 1
        if j > 0: p.append([i,j])
        i, j = i + 1, 0
    return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in p)


print(prime_factors2(7775460345233))
print(prime_factors2(7775460))
7775460
# print(prime_factors2(7919))
