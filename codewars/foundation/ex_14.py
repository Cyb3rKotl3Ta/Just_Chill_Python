def solution(text, ending):
    return text[len(text)-len(ending):len(text)] == ending

def solution2(string, ending):
    return string.endswith(ending)

print(solution('sum', 'asum'))

def solution3(text, ending):
    end_len = ending[::-1]
    text = text[::-1]
    return text[-1:end_len:] == ending

def solution4(string, ending):
    return ending in string[-len(ending):]

end_len = '890'[::-1]
res = '1234567890'[::-1]
# print()
print(res[:len()])
print(end_len)
if res[:3] == end_len:
    print("True")