# it has 2 sides sorted side and unsorted side
# works for len(arr)-1 times
# time complexity - O(n^2)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr
nums = [5, 4, 3, 2, 1]
insertion_sort(nums)
print(nums)



"""def insertion_sort(aaa):
    n = len(aaa)
    for i in range(1, n):
        j = i-1
        temp = aaa[i]
        while temp < aaa[j] and j >= 0:
            aaa[j + 1] = aaa[j]
            j -= 1
        aaa[j + 1] = temp
    return aaa"""