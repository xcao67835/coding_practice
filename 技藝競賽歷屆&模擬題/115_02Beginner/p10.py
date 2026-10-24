a=input()
i=0
while 1:
    find=bin(i)[2:]
    if find in a:
        i+=1
    else:
        break
print(i-1)