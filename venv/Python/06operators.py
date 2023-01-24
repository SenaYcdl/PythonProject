# 4 type of operators
# arithmetic
print(2 + 5)
# our opreator is +
# our operands is 2 and 5
# output 7

print("5+2=", 5 + 2)
print("5-2=", 5 - 2)
print("5*2=", 5 * 2)
print("5/2=", 5 / 2)
print("5**2=", 5 ** 2)
print("5//2=", 5 // 2)
print("5%2=", 5 % 2)

"""
5+2= 7
5-2= 3
5*2= 10
5/2= 2.5
5**2= 25
5//2= 2
5%2= 1
"""

# assignment
x = 5  # equivalent to x=5
x += 5  # equivalent to x+5
x - 5  # equivalent to x-5

# comparison(karsilastirma)

num1 = 10
num2 = 5
print(num1, ">", num2, "=", num1 > num2)
print(num1, ">=", num2, "=", num1 >= num2)
print(num1, "<", num2, "=", num1 < num2)
print(num1, "<=", num2, "=", num1 <= num2)
print(num1, "==", num2, "=", num1 == num2)
print(num1, "!=", num2, "=", num1 != num2)

"""
10 > 5 = True
10 >= 5 = True
10 < 5 = False
10 <= 5 = False
10 == 5 = False
10 != 5 = True
"""

# logical (and,or,not) true,false
# and bir false varsa sonuc false
print("true and false =", True and False)  # False
print("false and false and true =", False and False and True)  # False
print("false and true =", False and True)  # False
print("true and true =", True and True)  # True

# or bir true varsa sonuc true
print("true or false =", True or False)  # True
print("false or  false or true =", False or False or True)  # True
print("false or  true =", False or True)  # True
print("true or true =", True or True)  # True

# not
print("not true ", not True)  # false
print("not false ", not False)  # true
