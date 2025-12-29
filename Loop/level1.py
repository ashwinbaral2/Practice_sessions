"""
LOOPS – LEVEL 1 (Baby Steps 🍼)
A loop means: "do this again and again"
"""

# -----------------------------
# 1️⃣ Looping through numbers
# -----------------------------

numbers = [3, 2, 1, 4]

# Take ONE number at a time from the list
for item in numbers:
    print(item)

# Output:
# 3
# 2
# 1
# 4


# -----------------------------
# 2️⃣ Looping through names
# -----------------------------

names = ['puntu', 'barshafarsu', 'subububu', 'buneyy']

# ❌ This prints the FULL list again and again
for item in names:
    print(names)

# ✅ This prints ONE name at a time (correct way)
for item in names:
    print(item)

# ✅ Doing the same thing for each name
for item in names:
    print("Name detected!")


# -----------------------------
# 3️⃣ range() – counting numbers
# -----------------------------
# range(start, stop, step)

# start at 0
# stop BEFORE 3
# jump by 2

for num in range(0, 3, 2):
    print(num)

# Output:
# 0
# 2


# -----------------------------
# 4️⃣ Looping through a word
# -----------------------------

word = 'chikipiki-boom-boom'

# Take ONE letter at a time
for letter in word:
    print(letter)


# -----------------------------
# 5️⃣ enumerate() – index + value
# -----------------------------

colors = ['red', 'blue', 'green']

# enumerate gives:
# (index, value)

for color in enumerate(colors):
    print(color)

# Output:
# (0, 'red')
# (1, 'blue')
# (2, 'green')
