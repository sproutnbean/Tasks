#Function Definition
def sum_double (a, b):
    if a != b:
        return a + b;
    else:
        return 4*a

arg1 = 1
arg2 = 4

#Function Call    
print ("What is the sum double of ", arg1, " and ", arg2, " ?")
print (sum_double(arg1 ,arg2))
