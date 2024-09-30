#python program for largest among three
a=int(input("ENTER a value:"))
b=int(input("ENTER b value:"))
c=int(input("ENTER c value:"))
if a>b and a>c:
  print("A is greatest")
elif b>c:
  print("B is greatest")
else:
  print("c is greatest")
