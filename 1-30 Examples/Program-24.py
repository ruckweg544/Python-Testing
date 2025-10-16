# Program 24
# Description: Manually convert a decimal number to binary, octal and hexadecimal
# Date: 2025-10-14

''' ChatGPT Support for 'conversion_table' function'''
def conversion_table(num):
    # Prepare table content
    table = [
        ["Binary", bin(num)],         # R1
        ["Octal", oct(num)],          # R2
        ["Hexadecimal", hex(num)]     # R3
    ]

    # Compute max column widths for neat formatting
    col_widths = [max(len(row[c]) for row in table) for c in range(2)]
    for row in table:
        print("| " + " | ".join(f"{row[c]:<{col_widths[c]}}" for c in range(2)) + " |")

dec_num = int(input("Enter a decimal number: "))
conversion_table(dec_num)