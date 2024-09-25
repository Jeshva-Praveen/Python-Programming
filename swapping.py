#python program for swapping of two numbers
a=int(input("ENTER a value:"))
b=int(input("ENTER b value:"))
print("before swapping:")
print('values of a and b are:',a ,b )
a=a+b
b=a-b
a=a-b
print("after swapping:")
print('values of a and b are:',a,b)
