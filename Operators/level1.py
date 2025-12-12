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







''' 2. Comparison Operators (==, !=, >, <, >=, <=)'''
# Question: Check if a number is greater than 10.
# Example:
# == ------> Equal to
print(a == 10) #Output: False
# write code for other operators below here:
#-------------------------------------------







''' 3. Logical Operators (and, or, not) '''
# Question: Check if a number is between 5 and 15.
# Example:
print( a == 20 and b == 40) # True
# write code for other operators below here:
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








''' 6. Assignment Operators (=, +=, -=, *=, /=) '''
# Question: perform an operation on a variable by 10 using an assignment operator.
# Example:
a += 10 # equivalent to a = a + 10
print(a)  # a=20 and a = 20 + 10 ---> Output: 30
# write code for other operators below here:
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








''' 8. Ternary Operator '''
# Question: Assign a value to a variable based on a condition using a ternary operator.
# Example:
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
# write code for other operators below here:
#-------------------------------------------









''' 9. Walrus Operator (:=) '''
# Question: Use the walrus operator to assign and print a value in a single expression.
# Example:
if (n := 10) > 5:
    print(f"{n} is greater than 5")  # Output: 10 is greater than 5
# write code for other operators below here:
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






#------------------------------------------------
#End of file
#------------------------------------------------