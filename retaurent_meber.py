
name=input("enter cust name")
age=int(input("enter cust age"))
amount=int(input("enter bill amount"))
a=input("are you a member(y/n)")
if amount<=0:
    exit()
print(name)
print(age)
if a=="y":
    m_stat="member"
else:
    m_stat="guest"
print(m_stat)
if age>=18:
    a_stat="adult"
else:
    a_stat="minor"
print(a_stat)
if a=="y" and amount>=1000:
    discount=(amount*10/100)
    final=amount-discount
else:
    final=amount
print(final)