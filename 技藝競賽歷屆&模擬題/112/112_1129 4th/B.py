a,b=input().split()
win=("YO","OX","XY")
if a+b in win:
    print(2)
elif b+a in win:
    print(1)
else:
    print(0)