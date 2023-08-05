# Rosmael Zidane LEKEUFACK FOULEFACK

n = int(input('Enter your integer number : '))
s = input('Enter your word : ')

leng = len(s)

if leng < n :
	print("ERROR")
else :
	b = int(leng-n)
	mot = s[b:]
	print(mot)
