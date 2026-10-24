s=input().split()
s.sort(key=lambda x:len(x))
print(*s,sep=" ")