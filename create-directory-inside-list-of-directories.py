# Create a directory (based on user input) in a list od directories under /root/test5 directories.
# Except a NotADirectoryError error when dealing with files and just ignore the error and pass it.

import os
input1 = input("Enter the directory in yyyy format to be created")
lst = os.listdir(path='/root/test5')
print(lst)
for lst2 in lst:
    x = "/root/test5/" + str(lst2)
    try:
        os.chdir(x)
    except NotADirectoryError:
        pass 
    finally:
        os.mkdir(input1)
