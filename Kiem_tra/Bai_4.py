n=int(input())
a=list(map(int,input().split()))
while len(a)!=n:
    a=list(map(int,input().split()))
max=0    
for i in range(len(a)):
    if max<a[i]:
        max=a[i]
def xu_li(a,b):
    dem=0
    i=0
    while i<len(a):
        tam=0
        bingo=0
        for j in range(i+1,len(a)):
            if a[i]-a[j]<=0:
                dem+=tam
                i=j
                bingo=1
                break
            else:
                tam+=a[i]-a[j]
        if bingo==0:
            i+=1         

    print(dem)

xu_li(a,max)