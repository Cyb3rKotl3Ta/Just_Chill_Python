def lovefunc(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 != 0 or\
        flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    else: return False

def lovefunc_v2(flower1, flower2):
    return (flower1+flower2)%2

print(lovefunc(1,4))