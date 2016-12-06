import sys

#Function Definition
def monkey_trouble (a_smile, b_smile):
    if (a_smile and b_smile) or (not a_smile and not b_smile):
        return True;
    else:
        return False;

#Convert String to Boolean 
arg1 = False
arg2 = False

#Running Python in IDLE, disconnect this line if neccessary
sys.argv = ['monkey_trouble.py', 'True', 'True']
        
if ((sys.argv[1]) == 'True'):
    arg1 = True
else:
    arg1 = False
    
if ((sys.argv[2]) == 'True'):
    arg2 = True
else:
    arg2 = False

#Function Call    
print ("Got a Monkey Trouble? " )
print (monkey_trouble(arg1,arg2))
