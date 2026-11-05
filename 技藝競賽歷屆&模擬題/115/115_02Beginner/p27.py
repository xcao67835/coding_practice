s = set()
q = [[0]]
n = int(input())
a = 0
while q:
    i = q.pop()
    if  tuple(i) in s:
        continue
    s.add(tuple(i))
    sumi=sum(i)
    # print(sumi)
    if sumi-n==0:
        a+=1
        continue

    if n-sumi>=1:
        q.append(i+[1])
    if n-sumi>=2:
        q.append(i+[2])
    if n-sumi>=3:
        q.append(i+[3])

print(a)