import subprocess

readfile=open("/home/madhu/test2", 'r')

writefile=open("/home/madhu/test3", 'w')

#send the input from a file using stdin and write the output of cat command to another file using stdout
subprocess.run(["cat"], stdin=readfile, stdout=writefile)

readfile.close()

writefile.close()
