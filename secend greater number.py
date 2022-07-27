a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a>b and b>c:
    print(b)
elif c>a and a>b:
    print(a)
elif c>b and b>a:
    print(b)
elif b>a and a>c:
    print(a)