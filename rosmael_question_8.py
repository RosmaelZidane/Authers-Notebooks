 #Rosmael Zidane LEKEUFACK FOULEFACK
#creating a list 
l1=[4,1,3,7,5,6]
le = len(l1)
l2=[]*le

for j in range(le):
	prod = 1
	for k in range(le):
	  if j != k:
	     prod = prod*l1[k]
	l2 += [prod]
    
print(l2)	