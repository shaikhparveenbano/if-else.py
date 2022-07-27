cp=int(input("enter cos.price"))
sp=int(input("enter selling price"))
if sp>cp:
        print("profit",sp-cp)
else:
    print("loss",cp-sp)
