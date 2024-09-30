#Python program to evaluate the series 1/1!+2/2!+...+n/n!
n=int(input('Enter a number:'))
sum=0
fact = 1
for i in range(1,n+1):
  fact *= i
  sum=sum+i/fact
print(sum)
