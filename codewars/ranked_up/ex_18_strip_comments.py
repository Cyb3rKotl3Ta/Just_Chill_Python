

def strip_comments(strng, markers):
    return strng.strip(''.join(markers))

print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))



txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(''.join([',.grt"']))

# print(x)