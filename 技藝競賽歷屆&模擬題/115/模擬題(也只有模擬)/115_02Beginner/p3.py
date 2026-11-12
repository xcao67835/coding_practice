s=input()+"-"
m=0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        ss=s[i:j]
        if len(ss)>m:
            if ss==ss[::-1]:
                sss=ss
                m=len(ss)
print(sss)