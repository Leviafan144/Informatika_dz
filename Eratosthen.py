def Eratosthen(n):
    lst = [True]*(n+1)
    for i in range(2,n+1):
        if lst[i]:
            for j in range(i**2,n+1,i):
                lst[j]=False
    result=[i for i in range(n+1) if lst[i]]
    return result

a=int(input())
p=Eratosthen(10000)
print(p[a+1])