# Program 30
# Description: Natural Logarithm Calculator
# Date: 2025-10-15

import math

num = float(input("Enter a number: "))

while num <= 0:
    print("Enter a positive number.")
    num = float(input("Enter a number: "))
'''    if num > 0:
        break
'''
result = math.log(num)
print(f"The natural logarithm of {num} is: {result}")
