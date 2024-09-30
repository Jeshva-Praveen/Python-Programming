#Python program to find whether the given number is a palindrome or not
n=int(input('Enter a number: '))
temp=n
t=0
while temp!=0:
  t=t*10+(temp%10)
  temp//=10
if n==t:print(n,'is a PALINDROME')
else:print(n,'is NOT a PALINDROME')
