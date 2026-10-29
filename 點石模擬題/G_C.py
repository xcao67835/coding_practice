# -*- coding: utf-8 -*-
w="EXIT"
for _ in range(int(input())):

    indw=0
    s=input()
    for i in s:
        if i==w[indw]:
            indw+=1
        if indw==4:
            print("YES")
            break
    else:
        print("NO")
