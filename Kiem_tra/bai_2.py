s=input()
mang=s.split()
while len(mang)!=2:
    print("Nhập lại !!!!")
    s=input()
    mang=s.split()
a=int(mang[0])
b=int(mang[1])
def tinh(a,b):
    tien_tra=b-a
    dem=0
    i=1
    while tien_tra!=0:
        if tien_tra>=20:
            tam=tien_tra//20
            dem+=tam    
            tien_tra=tien_tra-tam*20
        elif tien_tra>=10:
            tam=tien_tra//10
            dem+=tam    
            tien_tra=tien_tra-tam*10
        elif tien_tra>=5:
            tam=tien_tra//5
            dem+=tam    
            tien_tra=tien_tra-tam*5
        elif tien_tra>=2:
            tam=tien_tra//2
            dem+=tam    
            tien_tra=tien_tra-tam*2
        elif tien_tra==1:
            tam=tien_tra
            dem+=tam    
            tien_tra=0
            dem+=tam  
            break 
    print(dem)
tinh(a,b)