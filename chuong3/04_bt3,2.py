a=int(input('M1='))
b=int(input('M2='))
c=int(input('M3='))
s=int(input('S='))

if s<=100:
    tiendien=a*s
elif s>=101 and s<=150:
    tiendien=(s-100)*b+100*a
else: 
    tiendien=100*a+(s-150)*c+50*b
print('Phai tra=',tiendien,sep='')
    


