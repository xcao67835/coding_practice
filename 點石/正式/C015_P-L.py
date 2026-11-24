n=int(input())
l=list(map(int,input().split()))
r=[-1]*n
idcr=[-1]*n
for i in range(n-2,-1,-1):
    pointer=i+1
    while l[i]>=l[pointer]:
        if pointer==-1:
            break
        pointer=idcr[pointer]
    else:
        r[i]=l[pointer]
        idcr[i]=pointer
    

print(*r)