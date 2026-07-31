a=int(input())
b=int(input())
def tr(x,n):
    dem=0
    while x>n:
        x-=n
        dem+=1
    return dem    
def tinh(a,b):
    tien_tra=a-b
    dem=0
    while tien_tra!=0:
        
        if tien_tra>20:
            dem+=tr(tien_tra,20)
        elif tien_tra>10:
            dem+=tr(tien_tra,10)
        elif tien_tra>5:
            dem+=tr(tien_tra,5)
        elif tien_tra>2:
            dem+=tr(tien_tra,2)
        else:
            dem+=tien_tra     
            tien_tra=0       
    print(dem)
tinh(a,b)