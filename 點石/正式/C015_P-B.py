ss=input()
s=[i for i in ss if i.isdigit() or i.isupper() or i.islower()]
s=[i.upper() if i.islower() else i for i in s]
print("YES" if s==s[::-1] else "NO")
n=""
for g in s:
    if g.isdigit():
        n+=g

if not n:
    print(-1)
else:
    n=int(n[::-1])

    print(n)