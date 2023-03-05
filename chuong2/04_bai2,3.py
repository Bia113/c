import math 
print('Nhap hai canh ke tam giac vuong:')
a=int(input())
b=int(input())
c=round(math.sqrt(a**2+b**2),2)
print('Canh ke thu nhat la: '+str(a)+' , '+'canh ke thu hai la: '+str(b)+' , '+'co canh huyen = ',c)