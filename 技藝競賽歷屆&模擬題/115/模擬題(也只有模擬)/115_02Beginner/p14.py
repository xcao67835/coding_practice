a,b = map(int,input().split())
bl=max(a,b)
if a>=b:
    for i in range(a,b-1,-1):
        print("-"*(bl-i) + "*"*i)
else:
    for i in range(a,b+1):
            print("-"*(bl-i) + "*"*i)
