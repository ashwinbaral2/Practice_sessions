# ============================================
# PYTHON DICTIONARY PRACTICE – LEVEL 1 TO 10
# ============================================

# Q1 (Level 1)
# Create a dictionary called student with keys: "name", "age", and "city"
# Assign any values you want and print the dictionary.
# ----------------------------------------------
# Your code here:
student = {"name": "John", "age": 21, "city": "New York"}
print(student)
# Output: {'name': 'John', 'age': 21, 'city': 'New York'}


# Q2 (Level 2)
# You are given:
boy = {"Name": "Ali", "Age": 20, "City": "Peshawar"}
# Update Ali's age to 22 using BOTH direct assignment and update()
# Then print the dictionary.
# ---------------------y---o------b----------------
# Your code here:

boy["City"]= "Kathmandu"
print(boy)

boy.update({"City": "Kathmandu"})
print(boy)


boy["Age"]=22
print(boy)

boy.update({"Age":23})
print(boy)


# Q3 (Level 3)
# Given this dictionary:
boy = {"Name": "Ali", "Age": 21, "Weight": 68}
# Add a new key "Religion" with value "Muslim"
# Then print only the keys of the dictionary using keys().
# ----------------------------------------------
# Your code here:

boy["Religion"]="Muslim"
print(boy)
print(boy.keys())
print(boy.values())
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

# Q4 (Level 4)

# Given:
boy = {"Name": "Ali", "Age": 21, "City": "Peshawar"}
# Safely access the value of "Height" using get().
# If it does not exist, return "Not Available".
# Print the result.
# ----------------------------------------------
# Your code here:
result=boy.get("Name")
print(result)

result=boy.get("Age")
print(result)

result=boy.get("City")
print(result)

result=boy.get("Height","not available")
print(result)

result=boy.get("Height","6 feet")
print(result)
# Q5 (Level 5)
# A dictionary cannot have duplicate keys.
# Create a dictionary with two 'City' keys and print the final output.
# Explain in a comment WHY the output appears the way it does.
# ----------------------------------------------
# Your code here:

boy = {"Name": "Ali", "Age": 21, "City": "Peshawar", "City":" Kathmandu"}
print(boy)


# Q6 (Level 6)
# Given:
boy = {"Name": "Ali", "Age": 21, "Weight": 68, "City": "Peshawar"}
# Remove the last inserted item using popitem() and print the dictionary.
# ----------------------------------------------
# Your code here:

# result=boy.popitem()
# print(boy)

# result=boy.popitem()
# print(result)

# result=boy.popitem()
# print(boy)

# result=boy.popitem()
# print(boy)

# result=boy.popitem()
# print(boy)
result=boy.popitem()
print(boy)

# result=boy.popitem()
# print(boy)
# Q7 (Level 7)
# Copy the following dictionary WITHOUT linking it to the original:
boy = {"Name": "Ali", "Age": 21, "City": "Peshawar"}
# Modify the copied dictionary (change Age)
# Confirm the original dictionary is unchanged.
# ----------------------------------------------
# Your code here:

boy_copy=boy.copy()
print(boy_copy)

boy_copy["Name"]="Aswin"
print(boy_copy)

# Q8 (Level 8)
# Create a nested dictionary called boys:
# boy1 = {"Name": "Ali", "Age": 23}
# boy2 = {"Name": "Ahmad", "Age": 21}
# boy3 = {"Name": "Abas", "Age": 22}
# Make a dictionary that contains all three as values.
# Then print Ahmad's age using dictionary indexing.
# ----------------------------------------------
# Your code here:

boys={"boy1":{"Name": "Ali", "Age": 23},"boy2":{"Name": "Ahmad","Age":21},"boy3":{"Name": "Abas","Age":22}}

result={boys["boy3"] ["Name"]}
print(result)
# Q9 (Level 9)
# Given this nested dictionary:
boys = {
    "boy1": {"Name": "Ali", "City": "Peshawar"},
    "boy2": {"Name": "Ahmad", "City": "Islamabad"},
    "boy3": {"Name": "Abas", "City": "Peshawar"},
}
# Write code that prints the names of all boys who live in Peshawar.
# ----------------------------------------------
# Your code here:


# Q10 (Level 10)
# You are given a messy nested structure:
boys_details = {
    "boy1": {"Name": "Ali", "Age": 23, "Weight": 69},
    "boy2": {"Name": "Ahmad", "Age": 21, "Weight": 70},
    "boy3": {"Name": "Abas", "Age": 22, "Weight": 72},
}
# Task:
# Write a loop that prints each boy's name and weight in this format:
# Ali weighs 69 kg
# Ahmad weighs 70 kg
# Abas weighs 72 kg
# ----------------------------------------------
# Your code here:

