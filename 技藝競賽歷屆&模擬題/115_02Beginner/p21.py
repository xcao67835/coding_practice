a = input()
a,o,b=a.split()
a,b = int(a),int(b)
ans=0

if o=="/":
    ans = a / b
    print(f"{ans:.3f}")
else:
    if o=="+":
        ans=a+b
    elif o=="-":
        ans=a-b
    elif o=="*":
        ans=a*b


    print(ans)