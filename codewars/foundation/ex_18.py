def count_positives_sum_negatives(arr):
    count_arr = [0, 0]
    if arr == []:
        count_arr.clear()
    for i in arr:
        if i > 0:
            count_arr[0] += 1
        else:
            count_arr[1] += i

    return count_arr

def count_positives_sum_negatives2(arr):
    if not arr: return []

    pos = 0
    neg = 0

    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x

    return [pos, neg]

def count_positives_sum_negatives3(arr):
  output = []
  if arr:
    output.append(sum([1 for x in arr if x > 0]))
    output.append(sum([x for x in arr if x < 0]))
  return output


print(count_positives_sum_negatives([]))
arr = []
print(arr == [])