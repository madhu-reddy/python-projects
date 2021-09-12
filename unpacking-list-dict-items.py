def mylearningsguru(a,b,c,d=0,e=0,f=0,g=0): #Positional parameters (a,b,c) and default parameters (e,f,g)
  print(f"value of a {a}"),
  print(f"value of b {b}"),
  print(f"value of c {c}"),
  print(f"value of d {d}"),
  print(f"value of e {e}"),
  print(f"value of f {f}"),
  print(f"value of g {g}")

mylist=[2,3]
mydict={"e":7,"f":8}
#using *mylist to unpack the list values and pass each list items as a positional argument.
#using **mydict to unpack the dict values and pass each dict item as a keyword argument.
mylearningsguru(5,*mylist,d=15,g=89,**mydict)
