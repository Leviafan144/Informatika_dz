#Способ 1
def LongestWord1(s):
    x=[[len(a),a] for a in s.split()]
    m=max(x)[0]
    return [i[1] for i in x if i[0]==m][0]

s=input()
print(LongestWord1(s))

#Способ 2
def LongestWord2(s):
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
print(LongestWord2(s))

