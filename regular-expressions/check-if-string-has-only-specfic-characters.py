# Write a Python program to check that a string contains only a certain set of characters (a-z, A-Z and 0-9). 

# 1st way to do it
import re 

reobj = re.compile(r'[A-Za-z0-9]*')
str1 = "Hithismadhumyemailistttgmail.com"
x = reobj.search(str1)
str2 = x.group()
if str1 == str2:
    print("string contains only a certain set of characters (in this case a-z, A-Z and 0-9)")
else:
    print("string contains other than a-z, A-Z and 0-9")



# 2nd way to do it
import re
def myfunc(data):
    reobj = re.compile(r'[^a-zA-Z0-9]')
    string = reobj.search(data)
    return not bool(string)

print(myfunc("myemailis@gmail.com")) 
print(myfunc("myemailisatgmaildotcom"))

