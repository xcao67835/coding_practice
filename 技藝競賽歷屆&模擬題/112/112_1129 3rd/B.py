win=["YO","OX","XY"]

a,b=input().split()
if a+b in win:
    print(2)
elif b+a in win :
    print(1)
else:
    print(0)