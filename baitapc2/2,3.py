import math
print ('Nhap hai canh ke cua ta giac vuong:')
a=int(input())
b=int(input())
c=math.sqrt(a**2+b**2)
print('Canh ke thu nhat la:',a,end=(','))
print(' Canh ke thu hai la:',b,end=(','))
print(' co canh huyen =',round(c,2))