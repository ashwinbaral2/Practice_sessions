# Parent class
class Barsha:
    eyes = "black"
    hair = "black"
    subject = "Microbiology"

# Child class
class Aashi(Barsha):
    subject = "Computer Science"  # overrides parent's subject

# Usage
print("Barsha's eyes:", Barsha.eyes)        # black
print("Barsha's hair:", Barsha.hair)        # black
print("Barsha's subject:", Barsha.subject)  # Microbiology

print("Aashi's eyes:", Aashi.eyes)          # black (inherited)
print("Aashi's hair:", Aashi.hair)          # black (inherited)
print("Aashi's subject:", Aashi.subject)    # Computer Science (child-specific)


class Aswin:
    Height = "6 feet"
    Face = "cute"
    Nose = "Sharp"
    Skin = "Fair"

class Ashraya(Aswin):
    Hair = "Golden brown"

print("Aswin's Face:", Ashraya.Face)
print("Aswin's Height:", Ashraya.Height)
print("Aswin's Nose:", Ashraya.Nose)

print("Ashraya's Nose:", Ashraya.Nose)
print("Ashraya's Hair:",Ashraya.Hair)
