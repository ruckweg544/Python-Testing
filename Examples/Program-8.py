# Program 8
# Description: Program that displays calendar of the month
# Date: 2025-10-13

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = calendar.month(year, month)
print(cal)