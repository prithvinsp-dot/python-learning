
def functionb(a):
    b=[]
    c=[]
    t=0
    for i in a:
        if i not in b:
            b.append(i)
        elif i in b and i not in c:
            c.append(i)
    for i in c:
        d=a.count(i)
        if d>t:
            t=d
            e=i
    return c,e,t
x=functionb([2,9,3,8,3])
print(x)
