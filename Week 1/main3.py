import numpy as np

def filled_bucket(buckets, i, soManyBuckets, waterLeft, L, used_buckets, counts):
    if waterLeft < 0:
        return

    if waterLeft == 0:
        L.append(used_buckets)
        counts.append(len(used_buckets))
        return

    for j in range(i, soManyBuckets):
        filled_bucket(buckets, j + 1, soManyBuckets, waterLeft - buckets[j], L, used_buckets + [buckets[j]], counts)


waterLeft = 9
myVolumes = [1, 1, 1, 1, 1, 2, 4, 5, 6]
soManyBuckets = len(myVolumes)
L = []
counts = []
filled_bucket(myVolumes, 0, soManyBuckets, waterLeft, L, [], counts)
print(L[0])
print(L[-1])
print("min = ", min(counts), "max = ", max(counts))