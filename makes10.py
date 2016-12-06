import sys

#Function Definition
def makes10(a, b):
  if a == 10 or b == 10 or a+b == 10:
    return True;
  else:
    return False;

#Input
arg1 = 10
arg2 = 10

#Function Call    
print ("Make 10? " )
print (makes10(arg1,arg2))
