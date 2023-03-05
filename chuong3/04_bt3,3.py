
x=float(input('Nhap so thuc x: '))
y=float(input('Nhap so thuc y: '))
ch=input('Phep toan:')

if ch=='/' :
    if y!=0:
        print(str(x)+'/'+str(y)+'=',x/y,sep='')
    else:
        print('Khong hop le')

elif ch=='+':
    print(str(x)+'+'+str(y)+'=',x+y,sep='')
elif ch=='-':
    print(str(x)+'-'+str(y)+'=',x-y,sep='')
elif ch=='*':
    print(str(x)+'*'+str(y)+'=',x*y,sep='')
else: 
    print('Khong hop le')




    
