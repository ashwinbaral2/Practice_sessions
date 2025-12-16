def numbers (greater, smaller):
    Minus = greater - smaller
    print(f"the subtraction result is {Minus}")

numbers(9,6)
numbers(6,9)


def digits(greater, smaller):
    if greater>smaller:
       print(f"the greater number is {greater}, the smaller number is {smaller}")
    else:
       print(f"the greater number is {smaller}, the smaller number is {greater}")

digits(7,9)
digits(99, 98)
digits(10000, 20000)
digits(9999, 999)
digits("gir", "boysss")
digits(True, False)
print(4%2)
print(11%2)


def numerical_values(num):
    if num%2 ==0:
        print(f"the {num} number is even")
    else:
        print(f" the {num} number is not even")

numerical_values(5)
numerical_values(6)

