# -*- coding: utf-8 -*-
from collections import defaultdict
c="A=10 台北市, J=18 新竹縣, S=26 高雄縣, B=11 台中市, K=19 苗栗縣, T=27 屏東縣, C=12 基隆市, L=20 台中縣, U=28 花蓮縣, D=13 台南市, M=21 南投縣, V=29 台東縣, E=14 高雄市, N=22 彰化縣, W=32 金門縣, F=15 台北縣, O=35 新竹市, X=30 澎湖縣, G=16 宜蘭縣, P=23 雲林縣, Y=31 陽明山, H=17 桃園縣, Q=24 嘉義縣, Z=33 連江縣, I=34 嘉義市, R=25 台南縣,"
cc = c.split(', ')
ccc=[i.split()[0] for i in cc]
cccc = [i.split("=") for i in ccc]
c = [[i[0], (int(i[1][0])+int(i[1][1])%10*9)%10] for i in cccc]

s=input()
su=0
for i in range(9):
    su+=int(s[i])*int("876543211"[i])
    
    
d = defaultdict(list)
for a,b in c:
    d[b].append(a)
print(*sorted(d[(10-su%10)%10]),sep="")