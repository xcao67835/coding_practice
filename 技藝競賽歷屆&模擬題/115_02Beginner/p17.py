h,w=map(int,input().split())
r,c=map(int,input().split())
s=input()
for i in s:
    if i=="U":
        r-=1
    elif i=="D":
        r+=1
    elif i=="L":
        c-=1
    elif i=="R":
        c+=1
    if not ((0<=r<=(h-1)) and (0<=c<=(w-1))):
        print("Game Over")
        break
else:
    print(r,c)