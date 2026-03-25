def merge_sort(a):
    n = len(a)
    if n == 1:
        return a
    mid = n // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

def merge(left, right):
    n = len(left)
    m = len(right)
    i = j = 0
    temp = []
    while i < n and j < m:
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    temp.extend(left[i:])
    temp.extend(right[j:])
    return temp

arr = [5, 4, 3, 2, 1]
print(merge_sort(arr))



######################################### without merge function #############################################
"""def merge_sort(a):
    n = len(a)
    if n == 1:
        return a
    mid = n // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    n = len(left)
    m = len(right)
    i = j = 0
    temp = []
    while i < n and j < m:
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    temp.extend(left[i:])
    temp.extend(right[j:])
    return temp

arr = [5, 4, 3, 2, 1]
print(merge_sort(arr))"""
