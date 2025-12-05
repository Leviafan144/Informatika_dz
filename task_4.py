def f(n,m):
    if n==0:
        return 0
    if m==0:
        return f(n-1,m)+1
    return f(n,m-1)+1

n=int(input())
m=int(input())
print(f(n,m))