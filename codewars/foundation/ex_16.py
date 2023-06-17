def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

def open_or_senior(data):
    res = []
    for (age, hendicup) in data:
        if age >= 55 and hendicup > 7:
            res.append("Senior")
        else:
            res.append("Open")
    return res
