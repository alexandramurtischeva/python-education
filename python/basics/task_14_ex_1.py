import re

find_members = []

for attribute in dir(re):
    if "find" in attribute:
        find_members.append(attribute)

find_members.sort()
print(find_members)
