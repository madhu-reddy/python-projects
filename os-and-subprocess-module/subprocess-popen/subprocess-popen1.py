import subprocess
p1=subprocess.Popen(["df -h"], shell=True)
p1=subprocess.Popen(["top"], shell=True)
#print(p1.returncode)
print(p2.wait())
if p2.returncode == 0:
   print("command: success")
else:
   print("command: failed")
