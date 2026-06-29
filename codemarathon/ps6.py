#6. Find the Sum of Digits

no=int(input("Enter no"))
rem=0
sum=0
while no>0:
    rem=no%10
    sum=sum+rem
    no=no//10

print("sum of digit=",sum)    



