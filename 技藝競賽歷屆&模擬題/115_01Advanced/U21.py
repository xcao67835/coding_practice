a = input()
ans=[]
for i in range(len(a)-1):
    ans.append(str(abs(ord(a[i])-ord(a[i+1]))))
    
print("".join(ans))