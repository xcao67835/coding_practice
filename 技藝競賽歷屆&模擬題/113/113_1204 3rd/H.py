# -*- coding: utf-8 -*-

d={"A":10, "J":18, "S":26, 
"B":11, "K":19, "T":27, 
"C":12, "L":20, "U":28, 
"D":13, "M":21, "V":29, 
"E":14, "N":22, "W":32, 
"F":15, "O":35, "X":30, 
"G":16, "P":23, "Y":31, 
"H":17, "Q":24, "Z":33, 
"I":34, "R":25}

s=input()
s = s.replace(s[0],str(d[s[0]]))

ans=0
for i in range(11):
    ans+=int(s[i]) * int("19876543211"[i])
    
if ans%10==0:
    print("Y")
else:
    print("N")