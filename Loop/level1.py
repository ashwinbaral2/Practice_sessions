# PRACTICE QUESTIONS — Nested If / Conditions
# -------------------------------------------
# Three practice problems similar to the shop‑discount question.
'''
# Q1. Movie Ticket Pricing
------------------------
# If age is above 60, check if they have a senior citizen card.
   - If yes → 50% discount
   - If no → 30% discount
# Else if age is between 18 and 60 → no discount
# Else (below 18): provide 20% student discount.
'''
age = int(input("Enter your age : "));
ticket_price = 400;

if 120 > age > 60 :
    senior_citizen_card = input("Do you have Senior Citizenship Card available? (yes/no) : ").strip().lower();
    
    if senior_citizen_card == "yes":
        discount = 0.5;
        print(f"You get the Discount of 50% . ");
    else:
        discount = 0.3;
        print(f"You get the Discount of 30% .");
        
elif 18 <= age <= 60 :
    print (f"No Discount Applied. ");
    
elif  1 <= age <= 18 :
    discount = 0.2;
    print(f"You get the Discount of 20% . ");
    
else: 
    discount = None;
    print(f"Entered age value is invalid ! ")

ticket_price *= 1 - discount;
print( f"Your total cost price for the ticket is {ticket_price}.");



age= int(input("enter the age of customer: "))
if age>=60:
    print("50% discount")
elif age <60 and age >18:
    print("no discount")

else:
    print("20% discount")




# Q2. Exam Eligibility Checker
# ----------------------------
# If attendance is above 75%, check if assignment submission is complete.
#   - If complete → print "Eligible for exam"
#   - Else → print "Submit assignments first"
# If attendance is below 75% → print "Not enough attendance"

attendance = float(input("Enter your attendance percentage: "))
if attendance > 75:
    assignments_complete = input("Are all assignments submitted? (yes/no): ").strip().lower()
    if assignments_complete == "yes":
        print("Eligible for exam")
    else:
        print("Submit assignments first")
else:
    print("Not enough attendance")



# Q3. Internet Package Selection
# ------------------------------
# If user chooses "premium" plan, check if they want annual billing.
#   - If yes → give 25% discount
#   - If no → no discount
# If user chooses "basic" plan → check if data usage is below 100GB
#   - If below 100GB → give 5% discount
#   - Else → no discount

plan = input("Choose your internet plan (premium/basic): ").strip().lower()
if plan == "premium":
    annual_billing = input("Do you want annual billing? (yes/no): ").strip().lower()
    if annual_billing == "yes":
        discount = 0.25
        print("You get a 25% discount on the premium plan.")
    else:
        discount = 0
        print("No discount applied on the premium plan.")
elif plan == "basic":
    data_usage = float(input("Enter your monthly data usage in GB: "))
    if data_usage < 100:
        discount = 0.05
        print("You get a 5% discount on the basic plan.")
    else:
        discount = 0
        print("No discount applied on the basic plan.")
else:
    discount = None
    print("Invalid plan selected.")
base_price = 1000 if plan == "premium" else 500
if discount is not None:
    final_price = base_price * (1 - discount)
    print(f"Your final price is: {final_price}")


