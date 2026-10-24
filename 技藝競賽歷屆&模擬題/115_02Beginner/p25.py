poison=0
hp,bosshp,bossatk=map(int,input().split())
n=int(input())

for i in range(n):
    t,str=input().split()
    str=int(str)
    dmgreduce=0
    bosshp-= poison*3

    if t=="FIRE":
        bosshp -= str
        bosshp -= 10
    elif t=="WATER":
        bosshp -= str
        hp+=5
    elif t=="THUNDER":
        bosshp -= str
        if (i+1)%3==0:
            bosshp -= str
    elif t=="EARTH":
        bosshp -= str
        dmgreduce=5
    elif t=="POISON":
        bosshp -= str
        poison+=1

    if bosshp<=0:
        print("Victory",end=" ")
        break

    hp-=max(0,bossatk-dmgreduce)

    if hp<=0:
        print("Defeat",end=" ")
        break

else:
    print("Draw",end=" ")

print(max(0,hp), max(0,bosshp))