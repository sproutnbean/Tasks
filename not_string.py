#Function Definition
def not_string(str):
  if str[:3] == "not":
    return str;
  else:
    return "not "+str;

arg1 = 'fun'

#Function Call    
print (not_string(arg1))
