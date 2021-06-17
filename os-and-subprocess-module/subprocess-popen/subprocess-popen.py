import subprocess

#subprocess.PIPE tells that a PIPE  should be opened  to the standard output stream  and it is assigned to variable a1
a1=subprocess.Popen(["ls", "-ltrh", "/home/madhu"], stdout=subprocess.PIPE)

#communicate() returns a tuple (stdout_data, stderr_data). The data will be strings if streams were opened in text mode; otherwise, bytes.
#first element in a tuple is stdout which we want to print & then decode the output from bytes to string. 
print(a1.communicate()[0].decode())


