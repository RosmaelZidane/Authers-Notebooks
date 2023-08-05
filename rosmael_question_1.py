
T = input('enter your string : ')
n = len(T)
c = int(n/2-1)
b = int(n/2+1)
k = int(n//2)

if n%2 == 0:
	print(T[c:b])
else :
	print(T[k])
