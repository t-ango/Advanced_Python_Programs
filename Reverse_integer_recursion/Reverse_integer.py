"""
Reverse Integer Using Recursion

This program reverses the digits of an integer using a recursive approach, demonstrating the power and simplicity of recursion.

Functions:
    - reverse_display(value): Recursively reverses the digits of an integer.
    - main(): Accepts user input and displays the reversed integer.

Features:
    - Uses recursion to break the problem into smaller subproblems.
    - Avoids built-in methods like string slicing, showcasing pure algorithmic logic.

Usage:
    - Run the program and enter an integer to see its reversed form.
"""

def reverse_display(value):
    if value < 10:
        return value
    else: 
        last_digit = value % 10
        other_digits = value // 10
        reverse_other_digits = reverse_display(other_digits)
        return int(str(last_digit) + str(reverse_other_digits))
        

def main ():
    integer = int(input("Enter an integer: "))
    reversed = reverse_display(integer)
    print (reversed)
    

main()



    


