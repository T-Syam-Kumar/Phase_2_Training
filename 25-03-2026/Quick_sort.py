def partition(arr , i ,pivot):
    j = pivot - 1

    while i<j:
        while arr[i] < arr[pivot]:
            i+=1
        while arr[j]>=arr[pivot]:
            j-=1
        if i < j:
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i] , arr[pivot] = arr[pivot] , arr[i]
    return i



def quick_sort(arr,l,r):
    if l<r:
        index = partition(arr,l,r)
        quick_sort(arr,l,index-1)
        quick_sort(arr,index+1, r)

nums = [9,5,7,1,67,3]
quick_sort(nums,0,len(nums)-1)
print(nums)






#===========   BUBBLE SORT =============
# def bubble(nums):
#
#     for phase in range(1, len(nums)):
#         for i in range(0, len(nums)- phase):
#             if nums[i] > nums[i+1]:
#                 nums[i] , nums[i+1] = nums[i+1 ] , nums[i]
#     return nums
# nums = [9,5,7,1,67,3]
# print( bubble(nums) )
#===========   SELECTION SORT =============
# def selection(nums):
#
#     for phase in range(len(nums)-1):
#         min = phase
#         for i in range(phase+1,len(nums)):
#             if nums[i]< nums[min]:
#                 min = i
#         nums[min] , nums[phase] = nums[phase] , nums[min]
#
#
#     return nums
# nums = [9,5,7,1,67,3]
# print( selection(nums) )
#===========   INSERTION SORT =============
# def insertion(nums):
#     for i in range(1,len(nums)):
#         j = i-1
#         temp = nums[i]
#         while j>=0 and nums[j] > temp:
#             nums[j+1] = nums[j]
#             j-=1
#         nums[j+1] = temp
#     return nums
#
# nums = [9,5,7,1,67,3]
# print( insertion(nums) )

#===========   MERGE SORT =============
#
# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid = len(arr)//2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#
#     i= 0
#     j = 0
#     temp = []
#     while i<len(left) and j < len(right):
#         if left[i] < right[j]:
#             temp.append(left[i])
#             i+=1
#         else:
#             temp.append(right[j])
#             j+=1
#     temp += left[i:] or right[j:]
#     return temp
#
#
#
#
# nums = [9,5,7,1,67,3]
# print( merge_sort(nums) )

#===========   QUICK SORT =============

"""def partition(arr , i ,pivot):
    j = pivot - 1

    while i<j:
        while arr[i] < arr[pivot]:
            i+=1
        while arr[j]>=arr[pivot]:
            j-=1
        if i < j:
            arr[i] , arr[j] = arr[j] , arr[i]
    arr[i] , arr[pivot] = arr[pivot] , arr[i]
    return i



def quick_sort(arr,l,r):
    if l<r:
        index = partition(arr,l,r)
        quick_sort(arr,l,index-1)
        quick_sort(arr,index+1, r)

nums = [9,5,7,1,67,3]
quick_sort(nums,0,len(nums)-1)
print(nums)
"""