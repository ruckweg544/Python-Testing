# Program 22
# Description: Least Common Multiple of two input number
# Date: 2025-10-14

def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if ((greater % x == 0) and (greater % y ==0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
print("The L.C.M. is", compute_lcm(num1, num2))

''' 
Python does not require variable declaraion at all
Variables don't have fixed tyes -- values do
At runtime, Python creates an object then refers to the object
'''