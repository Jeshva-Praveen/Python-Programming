#python program for finding leap year or not
a=int(input("Enter the year:"))
if a%4==0  and a%100!=0 or a%400==0:
    print("GIVEN YEAR",a,"IS A LEAP YEAR ")
else:
    print("GIVEN YEAR",a,"IS  NOT A LEAP YEAR ")
