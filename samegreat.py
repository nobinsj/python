"""Write a Python program to check whether the
given two numbers are same or not. If they are
not same, then check if the first number is
greater than second number."""

n1 = int(input(" Enter first number : "))
n2 = int(input(" Enter second number : "))

if(n1 != n2):
    print(" Numbers are not same")
    if(n1 > n2):
        print(" First number is Greater than Second number ")
    else:
        print(" Second number is Greater than First number ")
else:
    print(" Both numbers are same")
