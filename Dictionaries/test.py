name= "barsha"
email= "varshakoirala@gmail.com"
print(f"my name is {name}")
print(f"my email is {email}")

# Create a nested-if program for shop discount.
# If purchase is above 1000, check if customer has membership and provide 20% discount 
# if not member provide 10%.
# Print applicable discount.
# '''

purchase=int(input("enter amount of goods bought: "))
if(purchase>=1000):
    membership= input("do you have membership: (yes/no)")
    if (membership== "yes"):
     print("you get 20% discount")
    
    else:
     print("you get 10% discount")

else:
     print("you get no discount")




