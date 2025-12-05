from random import*

def first(x,n):
    m=x[0]+x[1]
    w=0
    for i in range(n-1):
        r=x[i]+x[i+1]
        if  r<=m:
            m=r
            w=i
    return [w,w+1]

def test(lst, res, n):
    if first(lst,n) == res:
        print("OK", lst)
    else:
        print('Error', lst)

#n=int(input())
#a=int(input())
#b=int(input())

#x=[randint(a,b) for i in range(n)]
#first(x)
test([0,1,2],[0,1],3)
test([0,0,0],[1,2],3)
test([-1,-1,3,2,-4,7],[3,4],6)