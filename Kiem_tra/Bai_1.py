n=int(input("Nhập vào số nguyên x : "))
a=[]
a=list(map(int,input().split()))
def mu(b,n):
    for i in range(n):
        b*=b
    return b
def tinh(n,a):
    tong=0
    for i in range (len(a)):
 
        tong+=a[i]*(n**(len(a)-1-i))
     
    print(tong)
tinh(n,a)


