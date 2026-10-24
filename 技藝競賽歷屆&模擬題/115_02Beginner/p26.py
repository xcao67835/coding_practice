d = dict()
n = int(input())
s=set()
ans=0
q = [[0,0,n]]
while q:
    aas,cop,nn=q.pop(0)
    if nn ==0:
        ans=max(ans,aas)
        continue

    if (aas,cop,nn) in s:
        continue

    s.add((aas,cop,nn))

    if nn>=2:
        q.append([aas,aas,nn-2])
    q.append([aas+1,cop,nn-1])
    q.append([aas+cop,cop,nn-1])
    # print(nn,len(q))
print(ans)