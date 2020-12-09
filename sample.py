txt = "hello world - git check"

print(txt)  # sample print

print("answer is : ", 2*5)

print("\n")  # newline

print("first-sentance", end=" ")  # print space instead of newline

print("second-sentance")

# string literal

name = "Abin"

college = "GECB\
Trivandrum"

print(name, "\n", college)

# numeric literal

x = 100

# Boolean literal

y = True

# Special literal

z = None

# variables

var1 = 20  # declare variable var1

var1 = "edited var1"  # re-declare variable var1

print(var1)

a = 5
b = 2
l = a/b
m = a//b
n = a**b
o = a % b
print("/ -> ", l, "   // -> ", m, "   ** -> ", n, "  % -> ", o)

val2 = input("Enter string : \n",)

print("you entered : ", val2, "type : ", type(val2),)

number = int(input("enter a integer "))

print(f"You enterd {number} and square is {number ** 2}")


a1 = int(input("Enter a number "))

if (a1 > 0):
    print("number u enterd is positive")
elif (a1 < 0):
    print("number u enterd is negative")
else:
    print("u entered zero")

if(a1 % 2 == 0):
    print("number is even")
else:
    print("number is odd")
