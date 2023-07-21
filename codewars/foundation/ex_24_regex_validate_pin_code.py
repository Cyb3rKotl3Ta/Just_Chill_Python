def validate_pin(pin):
    return pin.isdigit() and len(pin) == 4\
    or pin.isdigit() and len(pin) == 6

def validate_pin_v2(pin):
    return len(pin) in (4, 6) and pin.isdigit()

print(validate_pin('-12454'))