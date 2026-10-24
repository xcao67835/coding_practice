s = 'hello'
a = input().lower()

ind=0
for i in a:
    if i==s[ind]:
        ind+=1
    if ind==5:
        print("YES")
        break
else:
    print("NO")