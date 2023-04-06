#!/usr/bin/python3

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = input("Enter operation: ")
if c == '+':
    result = a+b
elif c == '-':
    result = a-b
elif c == '*':
    result = a*b
elif c == '/':
    result = a/b
print(f'The result is: {result}')

