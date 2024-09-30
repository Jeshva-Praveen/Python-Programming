#python program to check whether triangle is valid or not using sides
a=int(input("Enter side A:"))
b=int(input("Enter side B:"))
c=int(input("Enter side C:"))
if a+b>c and a+c>b and b+c>a:
  print("Triangle is valid")
else:
  print("Triangle is not valid")
