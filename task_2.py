#Способ 1
a = list(map(int, input().split()))
k=0
for i in range(len(a)):
    while a[i]<=0:
        a = a[:i]+a[i+1:]+[a[i]]
        k+=1
        if k >=len(a):
            break
    k+=1
    if k >= len(a):
        break
print(a)

#Способ 2
a = list(map(int, input().split()))
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
print(b+[0]*f+w)
