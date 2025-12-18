#Binary_search
'''def f(lst,n):
    lst=sorted(lst)
    r=len(lst)-1
    l=0
    while l<=r:
        m=(l+r)//2
        if lst[m]==n:
            return "YES"
        elif lst[m]>n:
            r=m-1
        else:
            l=m+1
    return "NO"

x,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in b:
    print(f(a,i))'''
#Binary_search with recursion
def f(lst,n,l,r):
    m = (l + r) // 2
    if lst[m] == n:
        return m
    if l>r:
        return 0
    if lst[m] > n:
        return f(lst, n, l, m - 1)
    return f(lst, n, m + 1, r)
x,n=map(int,input().split())
a=list(map(int,input().split()))
print(f(sorted(a),x,0,len(a)-1))