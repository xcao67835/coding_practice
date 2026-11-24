d={
"A":"A",
"E":"3",
"3":"E",
"H":"H",
"I":"I",
"J":"L",
"L":"J",
"M":"M",
"O":"O",
"S":"2",
"2":"S",
"T":"T",
"U":"U",
"V":"V",
"W":"W",
"X":"X",
"Y":"Y",
"Z":"5",
"5":"Z",
"1":"1",
"8":"8"

   }
def trans(s):
    for i in s:
        if i not in d:
            return False
    ss=s[::-1]
    for i in range(len(s)):
        if s[i]!=d[ss[i]]:
            return False
    return True
while 1:
    try:
        s=input()
        print(f"{s} -- ",end="")
        st=[0,0]
        if s==s[::-1]:
            st[0]=1
        if trans(s):
            st[1]=1
            
            
        if sum(st)==0:
            print("is not a palindrome.")
        elif sum(st)==2:
            print("is a mirrored palindrome.")
        elif st[0]==1:
            print("is a regular palindrome.")
        else:
            print("is a mirrored string.")
    except EOFError:
        break