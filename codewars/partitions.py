def partitions(n, I=1):
    yield [n]
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield [i,] + p
def combos(n):
    return list(partitions(n))