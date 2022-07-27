num=int(input("enter your class>:"))
if num>=1 and num<9:
    aim=input("what is your aim>:")
    if aim>"a" or aim>"A" and aim<"z" or aim<"Z":
        print(aim)
if num==10:
    sub=input("choose subject>:")
    if sub>"a" or sub>"A" and sub<"z" or sub<"Z":
        print(sub)
if num==11 and num==12:
    cl=input("choose coolege>:")
    if cl>"a" or cl>"A" and cl<"Z" or cl<"z":
        print(cl)    
