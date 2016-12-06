import sys

#Function Definition
def sleep_in(weekday, vacation):
    if (weekday is False) or (vacation is True) :
        return True
    else:
        return False

#Convert String to Boolean 
arg1 = False
arg2 = False

#Test argument, running Python in IDLE, disconnect this line if neccessary
sys.argv = ['sleep_in.py', 'True', 'True']
        
if ((sys.argv[1]) == 'True'):
    arg1 = True
else:
    arg1 = False
    
if ((sys.argv[2]) == 'True'):
    arg2 = True
else:
    arg2 = False

#Function Call    
print (sleep_in(arg1,arg2))
