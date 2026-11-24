for _ in range(int(input())):
    s=input()
    ans=0
    count=0
    for i in s:
        if i=="O":
            count+=1
            ans+=count
        else:
            count=0
    print(ans)