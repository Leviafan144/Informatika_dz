n=int(input())
a=list(map(int,input().split()))

for x in range(len(a)-1):
    m=a[0]
    for i in range(len(a)-x-1):
        if a[i]>=m:
            m=a[i]
            b=i
    a=a[:b]+a[b+1:]+[m]

print(*a)
