def LongestWord(s):
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
print(LongestWord(s))

