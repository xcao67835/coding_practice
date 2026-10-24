n,c=  map(int,input().split())
over=0
carry=0
maxi=0
for i in range(1,n+1):
    off,on=map(int,input().split())
    carry-=off
    carry+=on
    if over==0 and carry>c:
        over=i
    maxi=max(maxi,carry)
print(carry,over,maxi)