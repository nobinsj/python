"""write a program to check whether a given number is less than 5.
 if number is less than 5,
 print the square of the number"""

number = int(input(" Enter a number : "))

if(number < 5):
    print("\n Number you entered is less than 5 \n",
          f" Square of number you entered ({number}) : {number ** 2} ")
else:
    print("\n Number you entered is greater than or equals 5")
