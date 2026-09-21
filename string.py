
a=input("enter a sentence")
b=a.strip()
c=b.replace(" ","-")
e=c.find("a")
v=0
d=0
for i in c:
    if i in "aeiouAEIOU":
        v+=1
    elif i.isdigit():
        d+=1
print(c)
print(v)
print(d)
print(e)

    
