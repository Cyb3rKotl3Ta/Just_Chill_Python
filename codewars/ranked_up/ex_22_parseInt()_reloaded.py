from word2number import w2n
word_to_num = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
        'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
        'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
        'eighty': 80, 'ninety': 90, 'hundred': 100,
        'thousand': 1000, 'million': 1000000
    }

def parse_int(s):
    # Split words by space or hyphen
    words = [word for part in s.lower().split('-') for word in part.split()]
    total, current_number = 0, 0

    for word in words:
        if word in word_to_num:
            value = word_to_num[word]
            if value == 100:
                current_number *= value
            elif value >= 1000:
                total += current_number * value
                current_number = 0
            else:
                current_number += value

    total += current_number
    return total

# Examples
print(parse_int("one"))  # Output: 1
print(parse_int("twenty"))  # Output: 20
print(parse_int("two hundred"))  # Output: 200
print(parse_int("twenty-three"))  # Output: 23
print(parse_int("seven hundred eighty-three thousand nine hundred and nineteen"))  # Output: 783919

# just joking
words_to_number = lambda s: sum([int(w) if w.isdigit() else 0 if w == 'and' else (1 if w == 'one' else -1) * num for w, num in zip(s.replace('-', ' ').replace(' and ', ' ').split(), map('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split().index, ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'] + ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']))]) * (1 if 'million' in s else 1000000) + (1 if 'thousand' in s else 1000) * sum([int(w) if w.isdigit() else 0 if w == 'and' else (1 if w == 'one' else -1) * num for w, num in zip(s.split(), map('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split().index, ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'] + ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']))])
# print(w2n.word_to_num("two million three thousand nine hundred and eighty four"))

def parse_int_v2_false(s):
    cn, res = 0, 0
    for number in (word_to_num[w] for w in s.replace(' and','').split() if w in word_to_num):
        if   number <  100: cn += number
        elif number == 100: cn *= number
        else              : res += cn * number; cn = 0
    return res + cn

print(parse_int_v2("one"))  # Output: 1
print(parse_int_v2("twenty"))  # Output: 20
print(parse_int_v2("two hundred"))  # Output: 200
print(parse_int_v2("twenty-three"))  # Output: 23
print(parse_int_v2("seven hundred eighty-three thousand nine hundred and nineteen"))  # Output: 783919