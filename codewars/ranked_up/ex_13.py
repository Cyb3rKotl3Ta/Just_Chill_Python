import datetime


def make_readable(seconds):
    ss, mm, hh = 0, 0, 0
    return seconds


def make_readable2(seconds):
    # seconds = seconds % (24 * 3600) cut all hours to left remainder from division less than 24 hours in seconds
    hour = seconds // 3600  # amount of ours
    seconds %= 3600         #make remainder form division to count how much seconds left for minutes(60)
    minutes = seconds // 60
    seconds %= 60           #make remainder form division to count how much seconds left for seconds
    return "%02d:%02d:%02d" % (hour, minutes, seconds)
    # return f"{hour}:{minutes}:{seconds}" 

def make_readable3(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

def make_readable4(n):
    return f'{n//3600:02d}:{(n%3600)//60:02d}:{n%60:02d}'
# Driver program
n = 12
print(make_readable2(n))
# print(make_readable(22222222))

