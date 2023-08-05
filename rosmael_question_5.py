# Rosmael Zidane LEKEUFACK FOULEFACK
nbrn = int(input("Input your interger number n :"))
nbrm = int(input("Inter your interger number m :"))

l1 = [0]*nbrm
l2 = [0]*nbrm
#listn = [0]*nbrn
for i in range(nbrm):
    x = input("Inter your m number : ")
    l1[i] = x
    l2[i] =  int(l1[i])*nbrn
    
print(l2)