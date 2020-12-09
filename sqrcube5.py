"""write a program to check if the given number is greater than 5
If the number is greater than 5 then print the cube of the number
if the number is less than or equal to 5  then print the square of the number"""

number = int(input("Enter a number : "))

if(number > 5):
    print(f"\n number you entered [{number}] is greater than 5 \n",
          f" Cube of number[{number}] : {number ** 3}")
else:
    print(f"\n number you entered [{number}] is less/equals than 5 \n",
          f" Square of number[{number}] : {number ** 2}")
