s=input()
a=s.split()
m=input()
def xu_li(a,b):
    kt=0
    for i in range(len(b)):
        if a==b[i]:
            kt=1
            print(i,end=" ")
    if kt==0:
        print(-1)
xu_li(m,a)        