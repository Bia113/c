import math
r=int(input('Nhap vao ban kinh cua duong tron: '))
dientich=round(math.pi*r**2,1)
chuvi=round(2*r*math.pi,1)
print('Dien tich cua duong tron co ban kinh '+str(r)+' la =',dientich)
print('Chu vi cua duong tron co ban kinh '+str(r)+' la =',chuvi)
