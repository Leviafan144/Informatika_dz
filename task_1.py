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

def test(lst, res):
    if first(lst) == res:
        print("OK")
    else:
        print('Error', lst)

#n=int(input())
#a=int(input())
#b=int(input())

#x=[randint(a,b) for i in range(n)]
#first(x)