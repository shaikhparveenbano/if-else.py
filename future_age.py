birth_year=int(input("enter birth year>:"))
current_year=int(input("enter current year:>"))
future_year=int(input("enter future year>:"))
current_age=current_year-birth_year
if birth_year>0 and current_year>0:
    print(" current age=",current_year-birth_year)
if current_year>0 and future_year>0:
    print("future age=",future_year-current_year+current_age)



    