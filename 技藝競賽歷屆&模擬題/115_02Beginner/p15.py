n=int(input())
s=input()
while 1:
    combo,ind,cha =0,0,""
    for i in range(len(s)):
        if s[i]!=cha:
            cha=s[i]
            combo=1
            ind=i
        else:
            combo+=1
        if combo==n:
            s=s[:ind]+s[ind+n:]
            combo=0
            break
    else:
        break
if s:
    print(s)
else:
    print("EMPTY")