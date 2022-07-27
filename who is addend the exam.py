class_sd=int(input("enter number"))
class_attend=int(input("enter number"))
per=class_attend/class_sd*100
if per>=75:
    print("you are sit in exam",per)
elif per<=75:
    print("you are not sit in exam",per)