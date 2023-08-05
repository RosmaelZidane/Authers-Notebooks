#Rosmael Zidane LEKEUFACK FOULEFACK

# the prise is tick 
tick1 = 2000
age = int(input('Inter your age : ')) # the people can't be a float
if age < 70 and age >= 12 :
    tick = tick1
    print("your age is between [12,69]. the ticket is ",int(tick),"XAF for you")
elif age < 12 and age >= 0 : # age can't be negatif
    tick2 = tick1-(tick1*40)/100
    print("your age is between [0, 11]. the ticket is", int(tick2),"XAF for you")
elif age >= 70 :
    tick3 = tick1-(tick1*30)/100
    print("your age is between [70,70+]. the ticket is", int(tick3),'XAF for you')
else :
    print('you enter the age that is not valid: enter your age...')

# for the second point in this question

nageAD = int(input("how many of you are between the ages of [12,69] ? Inter the number : "))
nageAn = int(input("how many of you are between the ages of [0,11] ? Inter the number : "))
nageOl = int(input("how many of you are between the ages of [70,70+] ? Inter the number : "))

tickg1 = 2000
tpayg1 = tickg1*nageAD
tickg2 = tickg1 - (tickg1*40)/100
tpayg2 = tickg2*nageAn
tickg3 = tickg1 - (tickg1*30)/100
tpayg3 = tickg3*nageOl
totalpay = tpayg1 + tpayg2 + tpayg3
print("the total price paid by your group for your tickets is",totalpay,"XAF" )