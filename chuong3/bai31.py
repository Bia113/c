a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
max=a
min=c
if b>max and c<max:
    max=b 
    min=c 
elif b<max and b<min and a>c:
    max=a
    min=b
elif b<max and b<min and c>max:
    max=c
    min=b
elif b>max and c>max and b>min:
    max=b 
    min=a
elif c>max and b>max and b<min:
    max=c
    min=a
else:
    max=a
    min=c
print('SLN=',max,sep='')
print('SBN=',min,sep='')


    
    




