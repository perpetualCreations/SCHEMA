"""
Testing bold text parsing.
"""

sample = "Yes. ***Bold*** I am."

first = sample[:sample.find("***")] + "<strong><i>" + sample[sample.find("**") + 2:]
second = first[:first.find("***")] + "</i></strong>" + first[first.find("**") + 2:]
print(second)

index = 0
start_tag = False

