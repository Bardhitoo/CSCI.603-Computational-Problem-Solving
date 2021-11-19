def filled_bucket(target, s, myVolumes, combs, firInd, secInd):
    if firInd == (soManyBuckets - 1) and\
            secInd == (soManyBuckets - 1):
        print(combs)
        return 0

    while firInd < soManyBuckets and secInd < soManyBuckets:
        if s == target:
            s = 0
            secInd = firInd + 1
            firInd += 1

            filled_bucket(target, s, myVolumes, combs, firInd, secInd)
            return 0
        if s < target:  # myVolumes[index] < target and
            s += myVolumes[secInd]
            combs[firInd][secInd] = myVolumes[secInd]

            secInd += 1
            filled_bucket(target, s, myVolumes, combs, firInd, secInd)
            return 0

        if s > target:
            s -= myVolumes[secInd - 1]
            # s -= myVolumes[secInd - 2]
            # combs[firInd][secInd - 1] =
            combs[firInd][secInd - 2] = -1

            secInd -= 1
            filled_bucket(target, s, myVolumes, combs, firInd, secInd)
            return 0

    return -1


targetBucket = 8
myVolumes = [1, 1, 2, 4, 5, 6]
combinations = [[0 for x in range(len(myVolumes))] for y in range(len(myVolumes))]

minCombinations = False; myVolumes.sort(reverse=minCombinations)
soManyBuckets = len(myVolumes)
s = 0
index = 0

print(filled_bucket(targetBucket, s, myVolumes, combinations, 0, 0))


