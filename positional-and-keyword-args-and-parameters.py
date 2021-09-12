def mylearningsguru(a,*args,d=87,**kwargs):
  print(f"Value of a {a}")
  print(f"value of remaining positional arguments in form of a tuple {args}")
  print(f"value of d {d}")
  print(f"value of remaining keyword parameters in form of a dict {kwargs}")

mylearningsguru(5,2,3,d=67,e=78,f=90)

#output
"""
Value of a 5
value of remaining positional arguments in form of a tuple (2, 3)
value of d 67
value of remaining keyword parameters in form of a dict {'e': 78, 'f': 90}
"""
