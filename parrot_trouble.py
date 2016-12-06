import sys

#Function Definition
def parrot_trouble (talking, hour):
  if (talking and (hour < 7 or hour > 20)):
    return True;
  else:
    return False;

#Running Python in IDLE, disconnect this line if neccessary
sys.argv = ['parrot_trouble.py', 'True', 'True']

#Convert String to Boolean 
arg1 = False
arg2 = 9

if ((sys.argv[1]) == 'True'):
    arg1 = True
else:
    arg1 = False

#Function Call    
print ("Got Parrot Trouble? " )
print (parrot_trouble(arg1,arg2))
