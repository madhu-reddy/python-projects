'''
Using word character (\w) along with match group/groups
Most engines: "word character" matches ASCII letter, digit or underscore
'''

import re
match2groups = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(match2groups.group()) # Isaac Newton
print(f"{match2groups.group(1)} {match2groups.group(2)}") # Isaac Newton 

match3groups = re.match(r"(\w+) (\w+) (\w+)", "Isaac Newton physicist")
print(match3groups.group())
print(f"{match3groups.group(1)} {match3groups.group(2)} {match3groups.group(3)}")
