
a = [12, 7, 25, 4, 19, 31, 10, 18]
b=a[0]
c=a[0]
t=0
s=0
d=int(input("enter a number"))
FOUND=False
for i in a:
    if i>b:
        b=i
    if i<c:
        c=i
    if i%2==0:
        t+=1
    if i>10:
        s+=i
    if i==d:
        FOUND=True
print(b)
print(c)
print(t)
print(s)
if FOUND:
    print("gotchaa")
else:
    print("nahhhh")        