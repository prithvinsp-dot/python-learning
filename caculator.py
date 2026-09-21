
while True:
    print("1_add")
    print("2_sub")
    print("3_multiply")
    print("4_divide")
    print("5_exit")
    ch=input("enter a choice")
    n1=int(input("enter first number"))
    n2=int(input("enter second number"))
    if ch=="1":
        n=n1+n2
        print(n)
    elif ch=="2":
        n=n1-n2
        print(n)
    elif ch=="3":
        n=n1*n2
        print(n)
    elif ch=="4":
        n=n1/n2
        print(n)
    elif ch=="5":
        break
    else:
        print("invalid ch")
