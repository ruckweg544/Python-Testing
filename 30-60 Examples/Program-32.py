# Program 32
# Description: Sum of Array
# Date: 2025-10-15

arr = [1, 2, 3]

# Method 1: sum()
ans = sum(arr)
print('METHOD 1 Sum of the array is ', ans)

# Method 2: For loop
def sum_array(arr):
    total = 0
    for element in arr:
        total += element
    return total

result = sum_array(arr)
print('METHOD 2 Sum of the array is ', result)