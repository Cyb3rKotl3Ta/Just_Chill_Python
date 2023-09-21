from re import findall


def count_smileys(arr):
    count = 0
    smiles = ([':', ';'], ['-', '~'], [')', 'D'])
    for i in arr:
        if len(i) == 2:
            if i[0] in smiles[0] and i[1] in smiles[2]:
                count += 1
        if len(i) == 3:
            if i[0] in smiles[0] and i[1] in smiles[1] and i[2] in smiles[2]:
                count += 1
    return count

def count_smileys_v2(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))

def count_smileys_v3(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count


print(count_smileys([':D',':~)',';~D',':)']))