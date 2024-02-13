def selection_sort_one_pass(arr):
    size = len(arr)
    min_index = 0
    for num in range(1, size):
        if arr[num] < arr[min_index]:
            min_index = num

    arr[0], arr[min_index] = arr[min_index], arr[0]


array = [5, 2, 3, 4, 0, 1]
selection_sort_one_pass(array)
print(array)

import large_list

def filter_tuples(tup):
    ny_liste = []
    for i in tup:
        if i[0] + i[1] == i[2]:
            ny_liste.append(i)
    return ny_liste


a = (filter_tuples(large_list.liste))
print(a)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged


sorted_tuples = merge_sort(a)
print(sorted_tuples)


