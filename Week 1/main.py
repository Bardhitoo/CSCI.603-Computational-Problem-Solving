def filled_bucket(targetBucket, myVolumes, usedBuckets, index, minCombinations=False):
    if targetBucket == 0:
        for i in range(soManyBuckets):
            if usedBuckets[i] > 0:
                print(f"{usedBuckets[i]}L ", end='')
        print('\n')
        return 0

    while index < soManyBuckets:
        # go forward
        if (targetBucket >= myVolumes[index]) and (usedBuckets[index] != -1):
            usedBuckets[index] = myVolumes[index]
            targetBucket -= myVolumes[index]
            myVolumes[index] = 0

            index += 1

            filled_bucket(targetBucket, myVolumes, usedBuckets, index, minCombinations)
            return 0

        # go back
        elif (targetBucket < myVolumes[index]) and (usedBuckets[index] != -1) and (minCombinations==False):
            index -= 1

            # skip backward
            while usedBuckets[index] == -1:
                index -= 1

            myVolumes[index] = usedBuckets[index]
            targetBucket += usedBuckets[index]
            usedBuckets[index] = -1

            filled_bucket(targetBucket, myVolumes, usedBuckets, index, minCombinations)
            return 0

        # skip forward
        elif usedBuckets[index] == -1 or minCombinations==True:
            index += 1
            filled_bucket(targetBucket, myVolumes, usedBuckets, index, minCombinations)
            return 0

    print("No solution found!")

targetBucket = 9
myVolumes = [1, 1, 2, 4, 5, 6]
minCombinations = True; myVolumes.sort(reverse=minCombinations)
soManyBuckets = len(myVolumes)
usedBuckets = [0, 0, 0, 0, 0, 0]
index = 0

filled_bucket(targetBucket, myVolumes, usedBuckets, index, minCombinations=minCombinations)
