#8. Factorial of a Number  5 1*2*3*4*5=120 

no=int(input("Enter no="))

fact=1

for i in range(1,no+1):
   fact=fact*i
print("factorial of this no",fact)   