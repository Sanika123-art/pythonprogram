#5. Count the Digits in a Number  123 3  123456  6

N=int(input("Enter no"))
count=0

while N>0:   
    count=count+1
    N=N//10
print("digit in number=",count)     

