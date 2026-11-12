import itertools
a=input()
b=list(set(itertools.permutations(a)))
c=0
for i in b:
    for j in range(len(a)-1):
        if i[j]==i[j+1]:
            break
    else:c+=1
print(c)