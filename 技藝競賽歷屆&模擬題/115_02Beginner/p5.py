l=[i.strip() for i in input().split(",")]
l=list(map(lambda x:[ord(x[0]), int(x[1:])], l))
for j in range(2):
    for i in range(2):
        if l[0+j*2][i]>l[1+j*2][i]:
            l[0+j*2][i],l[1+j*2][i]=l[1+j*2][i],l[0+j*2][i]

a=((abs(l[0][0]-l[1][0])+1)*(abs(l[0][1]-l[1][1])+1)+(abs(l[2][0]-l[3][0])+1)*(abs(l[2][1]-l[3][1])+1))
if l[1][0]>=l[2][0] and l[1][1]>=l[2][1]:
    a-=(abs(l[1][0]-l[2][0])+1)*(abs(l[1][1]-l[2][1])+1)
print(a)