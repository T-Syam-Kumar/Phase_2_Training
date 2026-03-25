#Bubble big value to last by comparing adjacent values
# works for len(arr)-1 times
# time complexity - O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [5, 4, 3, 2, 1]
bubble_sort(arr)
print(arr)