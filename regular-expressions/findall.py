#Write a Python program that matches a string that has an a followed by zero or more b's.

import re 
reobj = re.compile(r'ab*')  
string = reobj.findall("he is absent abbsent today")
print(string) #['ab', 'abb', 'a']
