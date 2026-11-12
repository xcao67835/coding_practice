l=list(map(lambda x:int(x,2), input().split(",")))
r = max(l)-min(l)
a=bin(r)
print(a.count("1"))
