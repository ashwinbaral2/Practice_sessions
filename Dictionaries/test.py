#nested list
a= [1,2,3,4, [2,3,4], 5,6]


a= [1,2,3, [1,1,2,1,1,[1]]]
#output 1,2,3,1,1,2,1,1,1

# dictionary

#
data = {
    "name": "Suman",
    "address": "Nepal",
    "phone_number": [
        {"type": "NTC", "number": "9844"},
        {"type": "NCell", "number": "98062"},
    ],
}
print(f"{data['name']} {data['phone_number'][0]['type']} number is {data['phone_number'][0]['number']}")
#
# Suman NTC number is 9844
# Suman NCell number is 98062
# Access NTC number
print(data["phone_number"][0]["number"])  # 9844

# Access NCell number
print(data["phone_number"][1]["number"])  # 98062


# # ------------------ Nested Lists ------------------

# # Original nested lists
# a1 = [1, 2, 3, 4, [2, 3, 4], 5, 6]  

# # Another nested list example
# a2 = [1, 2, 3, [1, 1, 2, 1, 1, [1]]]

# # Goal: Flatten the nested list completely and print as a sequence
# # Output should be: 1,2,3,1,1,2,1,1,1

# def flatten(lst):
#     """Recursively flatten a nested list"""
#     result = []
#     for item in lst:
#         if isinstance(item, list):
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#     return result

# print(flatten(a2))  # [1, 2, 3, 1, 1, 2, 1, 1, 1]

# # ------------------ Dictionary ------------------

# data = {
#     "name": "Suman",
#     "address": "Nepal",
#     "phone_number": [
#         {"type": "NTC", "number": "9844"},
#         {"type": "NCell", "number": "98062"},
#     ],
# }

# # Goal: Print formatted phone info
# # Mistakes in original:
# # 1. Using double quotes inside f-string without escaping → broke string
# # 2. Used wrong key "phone number" instead of "phone_number"
# # 3. Extra incorrect lines at the end

# # Corrected prints:
# print(f"{data['name']} {data['phone_number'][0]['type']} number is {data['phone_number'][0]['number']}")
# # Output: Suman NTC number is 9844

# print(f"{data['name']} {data['phone_number'][1]['type']} number is {data['phone_number'][1]['number']}")
# # Output: Suman NCell number is 98062
