import sys

#Function Definition
def pos_neg(a, b, negative):
  if negative and a < 0 and b < 0:
    return True
  if not negative and a < 0 and b > 0:
    return True
  if not negative and a > 0 and b < 0:
    return True
  else:
    return False

#Running Python in IDLE, disconnect this line if neccessary
sys.argv = ['pos_neg.py', 'True']

#Input 
arg1 = -5
arg2 = -6

arg3 = False
        
if ((sys.argv[1]) == 'True'):
    arg3 = True
else:
    arg1 = False

#Function Call    
print (pos_neg(arg1, arg2, arg3))
