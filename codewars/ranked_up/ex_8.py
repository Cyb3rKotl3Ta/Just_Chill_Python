def pig_it(text: str):
    text = [i[1:] + i[0] + 'ay' for i in text.split()]
    for i in range(len(text)):
        if text[i][0] in list('''!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'''):
            text[i] = text[i][0]
            
    return ' '.join(text)

def pig_it2(text: str):
    return " ".join(i[1:] + i[0] + "ay" if i.isalnum() else i for i in text.split())


print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it('Hello world !'))     # elloHay orldway !