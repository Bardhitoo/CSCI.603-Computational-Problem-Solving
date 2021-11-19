import random


def selection_sort(data):
    for k in range(len(data) - 1, 0, -1):
        maxid = k
        for index in range(k):
            if data[index] > data[maxid]:
                maxid = index

        temp = data[k]
        data[k] = data[maxid]
        data[maxid] = temp


def merge_sort(data):
    if len(data) == 1:
        return data
    first = merge_sort(data[:len(data) // 2])
    second = merge_sort(data[len(data) // 2:])

    ans = []
    first_ind = 0
    second_ind = 0

    while first_ind < len(first) and second_ind < len(second):
        if first[first_ind] < second[second_ind]:
            ans.append(first[first_ind])
            first_ind += 1
        else:
            ans.append(first[second_ind])
            second_ind += 1

        if first_ind < len(first):
            ans.extend(first[first_ind:])

        if second_ind < len(second):
            ans.extend(second[second_ind:])

    return ans


a = [random.randint(0, 100) for _ in range(10)]

merge_sort(a)
