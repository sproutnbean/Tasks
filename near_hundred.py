#Function Definition
def near_hundred(n):
  dif1 = 100 - n;
  dif2 = 200 - n;
  
  if abs(dif1) <= 10 or abs(dif2) <= 10:
    return True;
  else:
    return False;

arg1 = 19

#Function Call    
print ("Is", arg1, "near 100?")
print (near_hundred(arg1))
