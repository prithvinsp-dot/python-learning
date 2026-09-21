
s=0
t=0
FOUND=False
a=int(input("enter how many"))
d=int(input("enter number to search"))
b=int(input("enter a number"))
b1=b
b2=b
if b%2==0:
    t+=1
if b==d:
    FOUND=True
for i in range(1,a):
    c=int(input("enter the number"))
    if c>b1:
        b1=c
    if c<b2:
        b2=c
    s+=c
    if c%2==0:
        t+=1
    if c==d:
        FOUND=True
print(b1)
print(b2)
print(s+b)
print(t)
if FOUND:
    print("target found")
else :
    print("not found")
        
