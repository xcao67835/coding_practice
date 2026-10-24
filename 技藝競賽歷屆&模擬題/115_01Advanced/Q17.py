l = []
for i in range(2,2+int(input())):
    l.append(int(input()))
    l.sort()
    if i%2==0:
        print(l[i//2-1])
    else:
        print((l[(i+1)//2-1] + (l[(i-1)//2-1]))//2)
