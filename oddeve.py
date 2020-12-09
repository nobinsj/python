"""Write a Python program to check whether or
not a given number is less than 50. If the
number is less than 50, then check if the
number is greater than 25 or not. If the number
is less that 25, then check whether the number
is odd or even."""

number = int(input(" Enter a number : "))

if(number < 50):
    print(f" The number[{number}] is less than 50")
    if(number > 25):
        print(f"  Number[{number}] greater than 25")
    else:
        print(f"   Number[{number}] is less than 25 ")
        if(number % 2 == 0):
            print("    Number is Even")
        else:
            print(f"    Number[{number}] is Odd")
else:
    print(f" Number[{number}] is greater than 50")
