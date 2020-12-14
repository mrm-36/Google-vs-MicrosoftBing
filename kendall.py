from itertools import combinations

def Kendall (listOne, listTwo):
    setOne = list(set(listOne))
    setOne.sort(key = listOne.index)
    setTwo = list(set(listTwo))
    setTwo.sort(key = listTwo.index)

    n = min(len(setOne), len(setTwo))
    setOne, setTwo = setOne[:n], setTwo[:n]

    reversions = 2 * len(set(combinations(setTwo, 2)).difference(set(combinations(setOne, 2))))
    kendall = 1 - 2 * reversions / (n*(n-1))
 
    return kendall