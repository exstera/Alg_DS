from array import DynamicArray
def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        element = arr.get(i)
        j = i - 1
        while j >= start and arr.get(j) > element:
            arr.set(j + 1, arr.get(j))
            j -= 1
        arr.set(j + 1, element)


def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = DynamicArray(), DynamicArray()
    for i in range(0, len1):
        left.append(arr.get(l + i))
    for i in range(0, len2):
        right.append(arr.get(m + 1 + i))

    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left.get(i) <= right.get(j):
            arr.set(k, left.get(i))
            i += 1
        else:
            arr.set(k, right.get(j))
            j += 1
        k += 1
    while i < len1:
        arr.set(k, left.get(i))
        k += 1
        i += 1
    while j < len2:
        arr.set(k, right.get(j))
        k += 1
        j += 1


def timsort(arr):
    min_run = 32
    n = arr.size()
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, n - 1))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(n - 1, start + size - 1)
            end = min(start + size * 2 - 1, n - 1)
            merge(arr, start, mid, end)
        size *= 2
    return arr

subsequence = DynamicArray()
subsequence.append(5)
subsequence.append(9)
subsequence.append(1)
subsequence.append(56)
timsort(subsequence).display()
