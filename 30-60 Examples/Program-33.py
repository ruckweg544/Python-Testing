# Program 33
# Description: Largest element in an Array
# Date: 2025-10-15

def largest_element(arr): 
    if not arr:
        return "Array is empty"
    largest_element = arr[0]

    for element in arr:
        if element > largest_element:
            largest_element = element
    
    return largest_element

my_array = [23, 3, 19, 7, 11, 13, 17, 2]
result = largest_element(my_array)
print(f"The largest element in the array is: {result}")