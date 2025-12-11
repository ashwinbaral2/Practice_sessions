# Python Questions Based on Different Operators (With One Solved Example Each)


a = 20
b = 40
''' 1. Arithmetic Operators (+, -, *, /, %)'''
# Question: Add two numbers and print the result.
#example solution:
sum = a + b
print(f"the sum of a and b is {sum}") #Output: the sum of a and b is 60

# write code for other operators below here:
#-------------------------------------------
difference = b - a
print(f"The difference of b and a is {difference}") # Output: The difference of b and a is 20
product = a * b
print(f"The product of a and b is {product}") # Output: The product of a and b is 800
quotient = b / a
print(f"The quotient of b divided by a is {quotient}") # Output: The quotient of b divided by a is 2.0
modulus = b % a
print(f"The modulus of b divided by a is {modulus}") # Output: The modulus of b divided by a is 0
#-------------------------------------------


''' 2. Comparison Operators (==, !=, >, <, >=, <=)'''
# Question: Check if a number is greater than 10.
# Example:
# == ------> Equal to
print(a == 10) #Output: False
# write code for other operators below here:
#-------------------------------------------
print(a != 10) # Output: True
print(a > 10)  # Output: True
print(a < 10)  # Output: False
print(a >= 20) # Output: True
print(a <= 15) # Output: False
#-------------------------------------------

''' 3. Logical Operators (and, or, not) '''
# Question: Check if a number is between 5 and 15.
# Example:
print( a == 20 and b == 40) # True
# write code for other operators below here:
#-------------------------------------------
print( a == 10 or b == 40) # True
print(not(a == 10)) # True
#-------------------------------------------
''' 4. Membership Operators (in, not in)'''
# Question: Check if 'apple' is in the fruits list.
# Example-1:
fruits = ['banana', 'apple', 'cherry']
print('apple' in fruits)  # True

# Example-2:
girls = ['barsha', 'eva' , 'matina']
if "barsha" in girls:
    print(" Meri maya who is the best and the prettiest! Loppa You")
else:
    print("meri maya ko sathi haru who are lucky to have her!")

# write code for other operators below here:
#-------------------------------------------
print('mango' not in fruits)  # True
print('eva' not in girls)  # False
#-------------------------------------------

''' 5. Identity Operators (is, is not) '''
# Question: Check if two variables refer to the same object.
# Example:
cutie  = 'barsha'
hottie = cutie
print( 'barsha' is hottie)  #true
print( 'barsha' is not hottie) # false
print('barsha' is cutie) # true
print('barsha' is not cutie) # false
# write code for other operators below here:
#-------------------------------------------
num1 = [1, 2, 3]
num2 = num1
print(num1 is num2)  # True
print(num1 is not num2)  # False   
#-------------------------------------------

''' 6. Assignment Operators (=, +=, -=, *=, /=) '''
# Question: perform an operation on a variable by 10 using an assignment operator.
# Example:
a += 10 # equivalent to a = a + 10
print(a)  # a=20 and a = 20 + 10 ---> Output: 30
# write code for other operators below here:
#-------------------------------------------
a -= 5  # equivalent to a = a - 5
print(a)  # a=30 and a = 30 - 5 ---> Output: 25
a *= 2  # equivalent to a = a * 2
print(a)  # a=25 and a = 25 * 2 ---> Output: 50
a /= 5  # equivalent to a = a / 5
print(a)  # a=50 and a = 50 / 5 ---> Output: 10.0
#-------------------------------------------

''' 7. Bitwise Operators (&, |, ^, ~, <<, >>) '''
# Question: Perform a bitwise AND operation between two numbers.
# Example:
x = 5  # In binary: 0101
y = 3  # In binary: 0011
result = x & y  # Bitwise AND
print(result)  # Output: 1 (In binary: 0001)

# write code for other operators below here:
#-------------------------------------------
result_or = x | y  # Bitwise OR
print(result_or)  # Output: 7 (In binary: 0111)
result_xor = x ^ y  # Bitwise XOR
print(result_xor)  # Output: 6 (In binary: 0110)
result_not = ~x  # Bitwise NOT
print(result_not)  # Output: -6 (In binary: ...11111010)
result_left_shift = x << 1  # Left Shift
print(result_left_shift)  # Output: 10 (In binary: 1010)
result_right_shift = x >> 1  # Right Shift
print(result_right_shift)  # Output: 2 (In binary: 0010)
#-------------------------------------------

''' 8. Ternary Operator '''
# Question: Assign a value to a variable based on a condition using a ternary operator.
# Example:
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
# write code for other operators below here:
#-------------------------------------------
score = 75
grade = "Pass" if score >= 50 else "Fail"
print(grade)  # Output: Pass
#-------------------------------------------

''' 9. Walrus Operator (:=) '''
# Question: Use the walrus operator to assign and print a value in a single expression.
# Example:
if (n := 10) > 5:
    print(f"{n} is greater than 5")  # Output: 10 is greater than 5
# write code for other operators below here:
#-------------------------------------------
if (m := 3) < 5:
    print(f"{m} is less than 5")  # Output: 3 is less than 5
#-------------------------------------------

''' 10. Exponentiation Operator (**)'''
# Question: Calculate the power of a number using the exponentiation operator.
# Example:
base = 2
power = 3
number = base ** power
print(number)  # Output: 8
# write code for other operators below here:
#-------------------------------------------
base2 = 5
power2 = 4 
number2 = base2 ** power2
print(number2)  # Output: 625

#------------------------------------------------
#End of file
#------------------------------------------------