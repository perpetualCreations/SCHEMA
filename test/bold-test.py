"""
Testing bold text parsing.
"""

sample = "When they don't get what they want, ***they grasp away with their sharp nails at our throats, until the ugly flesh is shown.***"

first = sample[:sample.find("***")] + "<strong><i>" + sample[sample.find("***") + 3:]
second = first[:first.find("***")] + "</i></strong>" + first[first.find("***") + 3:]
print(second)
