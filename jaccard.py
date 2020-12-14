def Jaccard(a, b):
    mp = {}
    for lst in [a, b]:
        for x in lst:
            if mp.get(x, 0) > 0: mp[x] += 1
            else: mp[x] = 1
    num = sum(1 for k in mp.values() if k == 2)
    denom = len(set(a + b))
    return num / denom