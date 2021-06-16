import subprocess
import re
out=subprocess.run(["ls", "-ltrh", "/home/madhu"],  capture_output=True, text=True)

out1=subprocess.run(["grep", "-i", "sss"], capture_output=True, text=True, input=out.stdout)

#split the text with /n as delimiter using split function of re module 
r1=re.split(r"\n", out1.stdout)
#print(r1)

print("All the matched files with name 'sss' in them under directory '/home/madhu' are:")
for x in r1:
    a1=x.split(' ')  #split the string "x" with space as delimiter and a list a1 is created
    print(a1[-1])    #print last element in the list a1
