import re
out=re.compile("madhu123*",re.IGNORECASE) #ignorecase and * means match preceding character zero more times

#Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding match object.
#If you want to locate a match anywhere in string, use search() instead of match()
a=out.search("rammadhu123fffffff")

#If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object.
#even in MULTILINE mode, re.match() will only match at the beginning of the string and not at the beginning of each line.
b=out.match(("rammadhu123ffffff"))
c=out.match("madhu123ffffffff")
print(a.group())
print(b)
print(c.group())

#output
'''
madhu123
None
madhu123
'''
