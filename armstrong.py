#Python program to find armstorng numbers
n=int(input('Enter a number: '))
sum = 0
temp = n
count=0
while temp!=0:
  temp//=10
  count+=1
temp=n
while temp > 0:
   digit = temp % 10
   sum += digit ** count
   temp //= 10
if n== sum:print(n,"is an Armstrong number")
else:print(n,"is not an Armstrong number")
