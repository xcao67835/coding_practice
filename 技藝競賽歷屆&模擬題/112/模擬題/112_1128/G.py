# -*- coding: utf-8 -*-
while 1:
    try:
        m,n=map(int,input().split(","))
        matrix=[]
        ans=0
        for i in range(m):
            tmp=list(map(int,input().split(",")))
            ans+=sum(tmp)
            matrix.append(tmp)
            
        changed=1
        while changed and (m>1 and n>1):
            changed=0
            tm=[]
            m-=1
            n-=1
            
            for i in range(m):
                tmp=[]
                for j in range(n):
                    if matrix[i][j]==matrix[i+1][j]==matrix[i][j+1]==matrix[i+1][j+1]==1:
                        ans+=1
                        changed=1
                        tmp.append(1)
                    else:
                        tmp.append(0)
                tm.append(tmp)
            matrix=tm
            
        print(ans)
        
    except EOFError:
        break