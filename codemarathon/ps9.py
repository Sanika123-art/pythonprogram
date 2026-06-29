#10. Check Whether a Number is Palindrome
#123==321 palin not 
#121==121 palin yes

no=int(input("Enter no="))
rev=0
N=no
rem=0
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10

if N==rev:
    print("no is palindrom")  
else:
    print("no is not palindrom")    
