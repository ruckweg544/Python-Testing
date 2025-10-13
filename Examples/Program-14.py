# Program 14
# Description: Determine whether a number is Prime Number or not.
# Date: 2025-10-13

import math

def is_prime_sqrt(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime_sqrt(num):
    print(f"{num}, is a prime number")
else:
    print(f"{num}, is not a prime number")