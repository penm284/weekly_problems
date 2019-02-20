def unique_in_order(arr):
    arr = []
    ordered = []
    for i in arr:
        arr.append(i)
    prev = 0
    for a in arr:
      if a != prev:
          ordered.append(a)
      prev = a
    return ordered
