# Program 34
# Description: Array Rotation
# Date: 2025-10-15

# d is a number of positions to rotate

def rotate_array(arr, d):
    n = len(arr)
    if d < 0 or d >= n:
        return "Invalid rotation value"
    rotated_arr = [0] * n
    for i in range(n):
        rotated_arr[i] = arr[(i+d) % n]
    return rotated_arr

arr = [1, 2, 3, 4, 5]

d = 3

result = rotate_array(arr, d)
print("Original Array: ", arr)
print("Rotated Array: ", result)