def persistence(num):
    count = 0

    while num >= 10:
        product = 1
        while num > 0:
            product *= num % 10
            print(f'product: {product}')
            num //= 10
            print(f'num: {num}')
        num = product
        count += 1
    
    return count


print(persistence(33))
