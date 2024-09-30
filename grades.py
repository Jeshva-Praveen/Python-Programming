#python program to find the grade based on marks
a=int(input("Enter marks:"))
if a>=90:
  print("Grade for",a,"is A")
elif a>=80 and a<90:
  print("Grade for",a,"is B")
elif a>=70 and a<80:
  print("Grade for",a,"is C")
elif a>=60 and a<70:
  print("Grade for",a,"is D")
elif a>=50 and a<60:
  print("Grade for",a,"is E")
else:
  print("Failed")
