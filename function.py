# A function is block of code which only runs when it is called. 
# In python we do not  use parentheses and curly brackets, we use indentation tabs or spaces 


# Create function

 # we also can pass argument like way name ='miraz'

# def sayHello(name):
    
    #  Prints hello and then name
    
#     print ('Hello'+ name)

# sayHello('Miraz')


#Return value

# def getSum(num1, num2):
#     total = num1 + num2
#     return total

# print(getSum(34,45))
#we also can

# numSum = getSum(3,4)

# print(numSum)


# def addOneToNum(num):
#     num +=1
#     return num

# num = 5

# new_num = addOneToNum(num)
# print (new_num)

getSum = lambda num1, num2: num1 + num2

print(getSum(9,2))

addOneToNum = lambda num: num + 1

print (addOneToNum(5))








