#python program to determine the day of a week
import datetime
a=int(input("Enter date:"))
b=int(input("Enter month:"))
c=int(input("Enter year:"))
date=datetime.date(c,b,a)
print(date.strftime("%A"))
