#Rosmael Zidane LEKEUFACK FOULEFACK
# the expression of its first derivative denoted by f′ 
#                 
#           f' = 1/cos^2(x) 
#
# the second derivative of f denoted by f”
#
#            f" = (2*sin(x))/cos^3(x)
#
import math
x = float(input('Enter the degre of your angle if need his tangente : '))
y = math.radians(x) # we use this line to convert the angle on radian : the argument may be a radian

f = math.tan(y)  # f
f1 = 1/(math.cos(y))**2 # f' of f
f2 = (2*math.sin(y))/((math.cos(y))**3)  # f" of f
print("Different results after coputation are :")
print("the value of f(x) for ",x,'is', f)
print("the value of derivate of f is :", f1)
print("the value of second derivate of f is :", f2)
