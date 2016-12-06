#Function Definition
def diff21(n):
  difference = 21 - n;
  if n > 21:
      return abs(difference)*2;
  return abs(difference);

arg1 = 19

#Function Call    
print ("What is the difference of ", arg1, " and 21?")
print (diff21(arg1))
