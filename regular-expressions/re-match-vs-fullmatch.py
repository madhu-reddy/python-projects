import re
out=re.compile("^madhu123*",re.IGNORECASE) #ignorecase
a=out.fullmatch("madhu123") # If the whole string matches the regular expression pattern, return a corresponding match object.
b=out.match("madhu124567888") # If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object.
if a:
  print("matched")
else:
  print("not matched")

print(a)
print(b)

#output
"""
matched
<re.Match object; span=(0, 8), match='madhu123'>
<re.Match object; span=(0, 7), match='madhu12'>
"""
