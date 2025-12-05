'''a = list(map(int, input().split()))
k=0
b=[]
w=[]
f=0
for i in range(len(a)):
    if a[i]>0:
        b+=[a[i]]
    if a[i]<0:
        w+=[a[i]]
    if a[i]==0:
        f+=1
    while a[i]<=0:
        a = a[:i]+a[i+1:]+[a[i]]
        k+=1
        if k >=len(a):
            break
    k+=1
    if k >= len(a):
        break
#print(b+[0]*f+w)
print(a)'''

'''def f(n,m):
    if n==0:
        return 0
    if m==0:
        return f(n-1,m)+1
    return f(n,m-1)+1

n=int(input())
m=int(input())
print(f(n,m))'''

'''def LongestWord(s):
    #x=[[len(a),a] for a in s.split()]
    #m=max(x)[0]
    #return [i[1] for i in x if i[0]==m][0]
    k=0
    m=0
    w=''
    for i in s:
        if i!=" ":
            k+=1
            w+=i
        else:
            if k>m:
                m=k
                d=w
            k=0
            w=''
    return d

s=input()
print(LongestWord(s))'''

from random import*

def first(x):
    m=x[0]+x[1]
    w=0
    for i in range(n-1):
        r=x[i]+x[i+1]
        if  r<m:
            m=r
            w=i
    print(x)
    print(w,w+1)

n=int(input())
a=int(input())
b=int(input())

x=[randint(a,b) for i in range(n)]
