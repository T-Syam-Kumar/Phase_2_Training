"""arr = [2,4,52,135,343,6,3,65,2]
key = 52
for i in range(len(arr)):
    if arr[i] == key:
        print(i+1)
        break
"""

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
        else:
            return -1
    return None
nums = list(map(int, input().split()))
key = int(input())
print(linear_search(nums, key))
