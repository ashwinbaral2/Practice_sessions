# ============================================
# PYTHON DICTIONARY PRACTICE – LEVEL 1 TO 10
# ============================================

# Q1 (Level 1)
# Create a dictionary called student with keys: "name", "age", and "city"
# Assign any values you want and print the dictionary.
# ----------------------------------------------
# Your code here:
student = {"name" : "aswin",'age' : 23 ,'city' : 'Naya Thimi'}
print(student);
# Output: {'name': 'John', 'age': 21, 'city': 'New York'}


# Q2 (Level 2)
# You are given:
boy = {"Name": "Ali", "Age": 20, "City": "Peshawar"}
# Update Ali's age to 22 using BOTH direct assignment and update()
# Then print the dictionary.
# ----------------------------------------------
# Your code here:
boy['Age'] = 22;#direct-assignment
boy.update({'Age': 23})#update() method
print(boy);

# Q3 (Level 3)
# Given this dictionary:
boy = {"Name": "Ali", "Age": 21, "Weight": 68}
# Add a new key "Religion" with value "Muslim"
# Then print only the keys of the dictionary using keys().
# ----------------------------------------------
# Your code here:
boy['Religion'] = 'Muslim';
print(boy.keys());
print(boy.values());

# Q4 (Level 4)
# Given:
boy = {"Name": "Ali", "Age": 21, "City": "Peshawar"}
# Safely access the value of "Height" using get().
# If it does not exist, return "Not Available".
# Print the result.
# ----------------------------------------------
# Your code here:
result = boy.get('Height', 'Not Available');
print(result);
result_a = boy.get("Age", "Not Available");
print (result_a);

# Q5 (Level 5)
# A dictionary cannot have duplicate keys.
# Create a dictionary with two 'City' keys and print the final output.
# Explain in a comment WHY the output appears the way it does.
# ----------------------------------------------
# Your code here:
boy["City"] = "Kathmandu"
print(boy);#{'Name': 'Ali', 'Age': 21, 'City': 'Kathmandu'}

student1 = {
    "Name" : "Puntu",
    "City" : "Bkt",
    "City" : "Ktm"
}
print (student1);
# The second "City" key overwrites the first one, so only "Ktm" remains.

# Q6 (Level 6)
# Given:
boy = {"Name": "Ali", "Age": 21, "Weight": 68, "City": "Peshawar"}
# Remove the last inserted item using popitem() and print the dictionary.
# ----------------------------------------------
# Your code here:
boy.popitem();
print(boy);

# Q7 (Level 7)
# Copy the following dictionary WITHOUT linking it to the original:
boy = {"Name": "Ali", "Age": 21, "City": "Peshawar"}
# Modify the copied dictionary (change Age)
# Confirm the original dictionary is unchanged.
# ----------------------------------------------
# Your code here:
boy_new = boy.copy()
print (boy_new);
boy_new["Age"] = 25
print("Original dictionary:", boy)
print("Copied dictionary:", boy_new)
# Output:
# Original dictionary: {'Name': 'Ali', 'Age': 21, 'City': 'Peshawar'}
# Copied dictionary: {'Name': 'Ali', 'Age': 25, 'City': 'Peshawar'}


# Q8 (Level 8)
# Create a nested dictionary called boys:
# boy1 = {"Name": "Ali", "Age": 23}
# boy2 = {"Name": "Ahmad", "Age": 21}
# boy3 = {"Name": "Abas", "Age": 22}
# Make a dictionary that contains all three as values.
# Then print Ahmad's age using dictionary indexing.
# ----------------------------------------------
# Your code here:
boys ={
    "boy1":{
        "Name": "Ali", "Age": 23
    }, 
    "boy2":{
        "Name": "Ahmad", "Age": 21
    },
    "boy3":{
        "Name": "Abas", "Age": 22
    }
}
print(boys);
# Accessing Ahmad's age
ahmad_age = boys["boy2"]["Age"]
print("Ahmad's Age:", ahmad_age);
# Output:
# Ahmad's Age: 21
#------------------------------------------------------------------

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
for key, info in boys.items():
    if info["City"] == "Peshawar": print(info["Name"]);

#more beginner friendly code;
if boys["boy1"]["City"] == "Peshawar":
    print(boys["boy1"]["Name"]);
if boys["boy2"]["City"] == "Peshawar":
    print(boys["boy2"]["Name"]);
if boys["boy3"]["City"] == "Peshawar":
    print(boys["boy3"]["Name"]);
# Output:
# Ali
# Abas
#------------------------------------------------------------------
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
for key in boys_details:
  Name =  boys_details[key]["Name"];
  Weight = boys_details[key]["Weight"];
  print (Name, "weighs", Weight ,"Kg." );



# Output:
# Ali weighs 69 kg
# Ahmad weighs 70 kg
# Abas weighs 72 kg