#Function Definition
def missing_char(str, n):
  front = str[:n]
  back = str[n+1:]
  return front + back

arg1 = 'TROLOLOLOLOLOL'
arg2 = 5

#Function Call    
print (missing_char(arg1, arg2))
