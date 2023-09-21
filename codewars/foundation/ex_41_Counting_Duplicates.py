def duplicate_count(text:str):
    count = 0
    text = text.lower()
    for i in text:
        if text.count(i) > 1:
            count += 1
            text = text.replace(i, '')
    return count

def duplicate_count_v2(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
        
print(duplicate_count('abcdea'))