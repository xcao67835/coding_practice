# for i in range(int(input())):
#     a1,b1=map(int,input().split())
#     a2,b2=map(int,input().split())
#     c1=pow(a1,a2,2)
#     c2=pow(b1,b2,2)
#     #print(a1**a2,b1**b2)
#     print(c1,c2)
#     print("N" if c1==c2==1 else "Y")

for i in range(int(input())):
    a1,b1=map(int,input().split())
    a2,b2=map(int,input().split())
    # c1=pow(a1,a2,2)
    # c2=pow(b1,b2,2)
    # #print(a1**a2,b1**b2)
    # print(c1,c2)
    print("N" if a1*b1%2==1 else "Y")