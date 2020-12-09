"""write a python program  to check whether or not the
given number is divisible by 10"""

number = int(input("Enter a number : "))

if(number % 10 == 0):
    print(f"\n  Number you entered [{number}] is divisible by 10")
else:
    print(f"\n  Number you entered [{number}] is not divisible by 10")
