def alphabet_position(text):
    result = []
    for char in text.lower():
        if char.isalpha():
            # ord('a') returns the ASCII value of 'a' (97),
            # so we subtract it from the ASCII value of the current character
            # to get the position of the letter in the alphabet.
            position = ord(char) - ord('a') + 1
            result.append(str(position))
    return ' '.join(result)

def alphabet_position_v2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())