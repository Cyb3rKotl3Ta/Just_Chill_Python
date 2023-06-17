import re

def printer_error(s):
    err_count = 0
    for err in s:
        if ord(err) > 109:
            err_count += 1
    
    return f"{err_count}/{len(s)}"

def printer_error2(s):
    return f'{len(re.sub("[a-m]","",s))}/{len(s)}'

def printer_error3(s):
  return f"{sum(c > 'm' for c in s)}/{len(s)}"

