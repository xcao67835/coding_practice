a,b=input().split("=")
a=list(a)
b=int(b)
rec=0
xi,yi,zi=a.index("X"),a.index("Y"),a.index("Z")
# print(a,b)
for x in range(1,19):
    for y in range(x+1,20):
        for z in range(y+1,21):
            a[xi]=str(x)
            a[yi]=str(y)
            a[zi]=str(z)
            if eval("".join(a))==b:
                rec+=1
print(rec)