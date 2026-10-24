a,b=map(int,input().split())
prec=[2]
for i in range(3,b):
    for j in prec:
        if i%j==0:
            break

        if j>(i**0.5+1):
            prec.append(i)
            break
    else:
        prec.append(i)

ans=0
for i in prec:
    if i>=a:
        ans+=1

print(ans)