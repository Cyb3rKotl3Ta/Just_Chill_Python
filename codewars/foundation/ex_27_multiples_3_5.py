def sum_multiples(num):
    if num < 0:
        return 0
    
    total_sum = 0
    
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    
    return total_sum