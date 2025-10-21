# Program 36
# Description: Monotonic Array
# Date: 2025-10-20

# A monotonic array is one that is entirely non-increasing or non-decreasing

def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False
        
    return increasing or decreasing

arr1 = [1, 2, 2, 3]
arr2 = [3, 2, 1]
arr3 = [1, 3, 2, 4]

print("arr1 is monotonic: ", is_monotonic(arr1))
print("arr2 is monotonic: ", is_monotonic(arr2))
print("arr3 is monotonic: ", is_monotonic(arr3))