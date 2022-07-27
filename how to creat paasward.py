print("creat paasward")
ch= str(input("enter alphabet"))
if ch>="a" or ch>="A" and ch<="z" or ch<="Z":
    digit=(input("enter digit"))
    if digit>="1" or digit<="10":
        sc=input("enter special charecter")
        if sc=="@" or sc=="#"or sc=="&" or sc=="*":
            print("your paasward")
            print(ch+digit+sc)
        else:
            print("this is not strong paasward")
            print("please creat strong paasward")
    else:
        print("invailed digit")
else:
    print("invailed ch")