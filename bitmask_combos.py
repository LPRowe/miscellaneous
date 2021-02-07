def combinations(arr):
    res = set()
    for i in range(1, 2**len(arr)):
        j = 0
        combo = []
        while i:
            if i & 1:
                combo.append(arr[j])
            i = i // 2
            j += 1
        res.add(tuple(combo))
    return sorted(res, key = lambda c: (len(c), c))


if __name__ == "__main__":
    arr = list(range(5))
    combos = combinations(arr)
    print(combos)