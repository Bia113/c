a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
max=a
min=c
if  c>max and b>max and b<min:
    min=a
    max=c 
elif c<max and b<min:
    min=b 
elif b>max and a>min:
    min=c
    max=b
elif b>max and a<min:
    max=b 
    min=a
elif c>max and b<max :
    min=b
    max=c
else:     
    min=c
    max=a  
print("SLN=",max,sep="")
print("SBN=",min,sep="")