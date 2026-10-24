m,n=map(int,input().split())

directions=[(1,0),(0,1),(-1,0),(0,-1)]
maze = []
q = [((0,0),0)]
for i in range(m):
    maze.append(list(input()))

while q:
    r,c=q[0][0]
    maze[r][c]=q[0][1]+1
    del(q[0])
    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if not ((0)<=nr<=(m-1) and (0)<=nc<=(n-1)):
            continue

        if maze[nr][nc]!=".":
            continue

        q.append(((nr,nc),maze[r][c]))

    if r==m-1 and c==n-1:
        break

# print(*maze,sep="\n")


q = [(m-1,n-1)]
val=maze[m-1][n-1]+1
while q:
    r,c=q[0]
    if maze[r][c] == val-1:
        val=maze[r][c]
        maze[r][c]="*"
    else:
        maze[r][c]="."
    del(q[0])

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if not ((0)<=nr<=(m-1) and (0)<=nc<=(n-1)):
            continue

        if type(maze[nr][nc])!=int:
            continue

        q.append((nr,nc))

    if r==0 and c==0:
        break
    # print(*maze,sep="\n")

for i in maze:
    print("".join(i))