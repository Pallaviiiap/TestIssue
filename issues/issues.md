Title: Program crashes when second number is 0

Description:
The calculator program crashes when the user enters 0 as the second number.

Steps to Reproduce:
1. Run calculator.py
2. Enter first number = 10
3. Enter second number = 0

Expected Behavior:
The program should display a message like:
"Cannot divide by zero"

Actual Behavior:
The program crashes with ZeroDivisionError.

Possible Fix:
Handle division by zero inside the divide function.