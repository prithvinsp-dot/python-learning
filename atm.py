
b=1000
while True:
    print("1_check balance")
    print("2_deposit")
    print("3_withdraw")
    print("4_exit")
    ch=int(input("enter choice"))
    if ch==1:
        print(b)
    elif ch==2:
        a=int(input("enter amount"))
        if a>0:
            b+=a
            print(b)
        else:
            print("nvalid amount")
    elif ch==3:
        a=int(input("enter amount"))
        if a<=0:
            print("invalid")
        elif a>b:
            print("no balance")   
        else:
            b-=a
            print(b)
    elif ch==4:
        break
    else:
        print("invalid")