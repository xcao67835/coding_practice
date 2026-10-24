l = list(map(int,input().strip(" ").split(",")))
t = int(input())
a = 0
for i in range(2**len(l)):
    bi = "".join(bin(i)[2:]).zfill(len(l))
    # print(bi)
    tl=[]
    for ii in range(len(l)):
        tl.append(l[ii]*(int(bi[ii])*2-1))
    # print(tl)
    if sum(tl)==t:
        a+=1
print(a)