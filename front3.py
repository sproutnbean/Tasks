#Function Definition
def front3(str):
  if len(str) < 3:
    return str*3;
  
  return str[0:3]*3;

arg1 = 'TROLOLOLOLOLOL'

#Function Call    
print (front3(arg1))
