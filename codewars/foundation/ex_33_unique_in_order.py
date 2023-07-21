def unique_in_order(sequence):
    new_list = []
    for item in sequence:
        if len(new_list) < 1 or not item == new_list[len(new_list) - 1]:
            new_list.append(item)
    return new_list

def unique_in_order_v2(sequence):
    unique_sequence = []
    for item in sequence:
        if len(unique_sequence) == 0 or item != unique_sequence[-1]:
            unique_sequence.append(item)
    return unique_sequence

print(unique_in_order_v2('AAAABBBCCDAABBB'))