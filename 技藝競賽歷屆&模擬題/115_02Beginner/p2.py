d={"1":5, "2":3, "3":9, "4":7, "5":0, "6":8, "7":2, "8":1, "9":4, "0":6}
s=list(input().split("+"))
for i in range(2):
    s[i]=list(map(lambda x:str(d[x]),s[i]))
    s[i]="".join(s[i])

print(eval(s[0]+"+"+s[1]))