a=eval(input())
n=False
if a<0:
    n=True
    a = abs(a)

a = str(a)
a = list(reversed(a))
while 1:
    if a[0]=="0":
        del(a[0])
    else:
        break
a = "".join(a)
if a:
    a = eval(a)
else:
    a=0
if a%1==0:
    a=int(a)
if n:
    a=-a

print(a)