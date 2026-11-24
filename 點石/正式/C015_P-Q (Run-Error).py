from collections import Counter, defaultdict
import heapq
s=input()
# r=[]
# n=""
# for i in s:
#     if i.isdigit():
#         n+=i
#     else:
#         if n:
#             r.append(str(int(n)))
#             n=""
#         r.append(i)
# if n:
#     r.append(str(int(n)))
#     n=""
# tr=""
# for i in r:
#     tr+=i
# r=tr
r=s
chart=defaultdict(str)
rc=list(Counter(r).items())
rc=[[i[1], [i[0]]] for i in rc]
#print(rc)
heapq.heapify(rc)

while len(rc)!=1:
    a=heapq.heappop(rc)
    for i in a[1]:
        chart[i]="0"+chart[i]
        
    b=heapq.heappop(rc)
    for i in b[1]:
        chart[i]="1"+chart[i]

    heapq.heappush(rc,[a[0]+b[0], a[1]+b[1]])

#print(chart)
a1=0
for i in r:
    a1+=len(chart[i])
print(a1)

aa=input()
now=""
op=""
c=dict()
for a,b in list(chart.items()):
    c[b]=a
for i in aa:
    now+=i
    if now in c.keys():
        op+=c[now]
        now=""

op=list(op)
while op[0]=="0":
    op.pop(0)
op="".join(op)
print(eval(op))
