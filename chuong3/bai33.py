a=int(input('Tieu thu='))
if a>=1 and a<=100:
    b=550
elif a>=101 and a<=150:
    b=100*550+(a-100)*750
elif a>=151 and a<=200:
    b=100*550+50*750+(a-150)*950
else:
    b=100*550+(a-100)*750+(a-150)*950+(a-200)*1350
VAT=b*0.1
print('Phai tra=',b+VAT,sep='')
