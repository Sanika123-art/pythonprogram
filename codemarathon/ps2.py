#2. Print Even Numbers from 1 to N

N=int(input("Enter no for printing"))

'''for i in range(2,N+1,2):
    print("Even no=",i)'''

for i in range(1,N+1):
    if i%2==0:
        print("Even no=",i)
    else:
        print("odd no=",i)   
