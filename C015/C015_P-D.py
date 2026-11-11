n=input()
idx=0
mx=0
now=0
for i in range(len(n)):
    if n[i]=="0":
        now+=1
        if now>mx:
            idx=i-now+2
            mx=now
    else:
        now=0


print(mx)
if mx==0:
    print(-1)
else:
    print(idx)