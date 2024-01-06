# leap year determinant
year = int(input("Enter year in this format e.g., 2000. "))
if year % 4 == 0:
    print("This year is a leap year")
    if year % 100 == 0:
        print("This year is not a leap year")
        if year % 400 == 0:
            print("This year is a leap year")
        else:
            print("This year is not a leap year")
    else:
        print("This year is a leap year")
else:
    print("This year is not a leap year")