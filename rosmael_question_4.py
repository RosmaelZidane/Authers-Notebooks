# Rosmael Zidane LEKEUFACK FOULEFACK
n = int(input("Enter the number of the lenght that you will use : "))
listi = [0]*n
for j in range(n):
    listi[j] = input("Enter the numbers for this list  : " )
     
c = listi[0]
listi[0]= listi[n-1]
listi[n-1] = c
print(listi)    