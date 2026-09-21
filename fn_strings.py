
def sentence(a):
    b=a.split()
    Found=False
    t=0
    v=0
    d=[]
    e=[]
    for i in b:
        c=len(i)
        if Found==False:
            t=c
            l=i
            Found=True
        elif c>t:
            t=c
            l=i
    for i in a:
        if i in "aeiouAEIOU":
            v+=1
    for i in b:
        if i not in e:
            e.append(i)
        elif i not in d:
            d.append(i)
    return l,v,d
x=sentence("hello bro hi")
print(x)