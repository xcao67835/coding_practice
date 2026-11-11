m,n=map(int,input().split())
g=[]
for i in range(m):
    g.append(input().split())
stack=[]
for i in range(m):
    for j in range(n):
        stack.append((i,j))
while stack:
    changed=0
    i,j=stack.pop()
    if not (0<=i<m and 0<=j<n):
        continue


    if g[i][j]=="0":
        if j>0 and j<n-1:
            if g[i][j+1]!="0" and g[i][j-1]!="0":
                g[i][j]="b"
                changed=1
                stack+=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        if i>0 and i<m-1:
            if g[i+1][j]!="0" and g[i-1][j]!="0":
                g[i][j]="b"
                changed=1
                stack+=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

for i in g:
    print(*i)