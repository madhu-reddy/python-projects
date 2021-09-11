import random
min=0
max=6
rolling=input("Enter 'yes' if you want to continue rolling dice game")

while rolling == "yes" or rolling == 'y':
  print(random.randint(min,max))
  rolling = input("Enter 'yes' if you want to continue rolling dice game")
  
print("stopping roll dice game")
