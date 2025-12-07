n=int(input())
a=list(map(int,input().split()))

for i in range(1,len(a)):
    for j in range(i-1,-1,-1):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
            print(*a)
        i-=1