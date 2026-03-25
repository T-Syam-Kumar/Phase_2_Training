# opposite to bubble sort always keeps the small into front place
# works for len(arr)-1 times
# time complexity - O(n^2)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
arr = [5, 4, 3, 2, 1]
selection_sort(arr)
print(arr)