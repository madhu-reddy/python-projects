import subprocess
#result will be bytes format (as we have not used text=True, capture_output is used to store output in a variable)
output=subprocess.run(["ls", "-l"], capture_output=True)

#input parameter takes input from the stdout of above command (we need to use "stdin" instead of "input", when input is from a file or provided  at runtime)
filter=subprocess.run(["grep", "mylearningsguru.pdf"], input=output.stdout, capture_output=True)

#the "filter" variable contains stdout in bytes format, so we need to decode it to str format for better visibility
print(filter.stdout.decode('utf-8'))
