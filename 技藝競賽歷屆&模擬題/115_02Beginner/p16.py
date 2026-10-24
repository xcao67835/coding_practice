n=int(input())
def f(x):
    if x==0 or x==1:
        return 1
    else:
        return f(x-1)+f(x-2)

print(f(n))