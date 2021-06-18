import subprocess

a1=subprocess.Popen(["cp", "-rp", "/home/madhu/test2", "/home/madhu/test4"], stdout=subprocess.PIPE)
print(a1.returncode)
print(a1.pid)
print(a1.args) #['cp', '-rp', '/home/madhu/test2', '/home/madhu/test4']

a2=subprocess.Popen(["ls", "-ltrh", "/tmp"], stdout=subprocess.PIPE, text=True)
a3=subprocess.Popen(["ls", "-ltrh", "/tmp"], stdout=subprocess.PIPE, text=True)

#output of below commands are same, they are just different ways to read the standard output stream
print(a2.communicate()[0])
print(a3.stdout.read())


#subprocess.PIPE tells that a PIPE  should be opened  to the standard output stream  and it is assigned to variable a1
a4=subprocess.Popen(["ls", "-ltrh", "/home/madhu"], stdout=subprocess.PIPE)

#communicate() returns a tuple (stdout_data, stderr_data). The data will be strings if streams were opened in text mode; otherwise, bytes.
#first element in a tuple is stdout which we want to print & then decode the output from bytes to string (as we have not used shell=True)
print(a4.communicate()[0].decode())


