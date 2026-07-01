#set
'''number={10,20,30}
print(number)'''

#unorder
'''number={10,20,30}
print(number[0])'''

#unique
'''number={10,20,30,10,20}
print(number)'''

'''number={10,20,30}
for i in number:
    print(i)'''

#add
'''number={10,20,30}
number.add(40)
print(number)#10 20 30 40'''



#update

'''number={10,20,30}
number1={70,80}
number.update(number1)
print(number)'''


#remove


'''number={10,20,30}
number.remove(60)#10 20
print(number)'''

#discard

'''number={10,20,30}
number.discard(50)
print(number)'''

#pop
'''number={10,20,30}
number.pop()
print(number)'''


#clear

'''number={10,20,30}
number.clear()
print(number)#{}'''

#copy

'''number={10,20,30}
number1=number.copy()
print(number)
print(number1)'''


#union

'''number={10,20,30}
number2={40,20,50}#10 20 30 40 50 
number3=number.union(number2)
print(number3)'''

#intersection
'''number={10,20,30,50}
number2={40,20,50}#20 50
number3=number.intersection(number2)
print(number3)'''

#difference
number={10,20,30,50}
number2={40,20,50}#10 30
number3=number.difference(number2)
print(number3)













