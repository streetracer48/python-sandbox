# If / Else conditions are used to decide to do something based on something being true or false

x=56
y=55


#Comparison Operators( ==, !=, >, <, >=, <=) - used to compare values

#simple if

# if x == y :
#     print (f'{x} is equal to {y}')

#if else 

# if x > y :
#     print (f'{x} is greater than {x}')

# else :
#     print (f'{x} is less than {y}')

#elif

# if x > y :
#     print (f'{x} is greater than {y}')

# elif x==y :
#     print (f'{x}  is equal to {y}')

# else:
#   print (f'{x} is less than {y}')

#Nested if else

# if x > 2:
#      if x <= 10:
#         print (f'{x} is greater than 2 but {x} is less than 10');
#      else:
#          print (f'{x} is  greater than 2 but {x} is not less than 10 ')

# else:
#      print(f'{x} is less than 2')         



#Logical Operators(and, or, not) - Used to combine conditional statements

#and 

# if x > 2 and x <= 10 :
#     print (f'{x} is greater than 2 and {x} is less than 10');

# else: 
#     print ('Condition false')

# or

# if  x > 2 or x <= 10 :
#     print (f'{x} is greater than 2 or {x} is less than 10')

#not 

# if not(x == y):
#     print(f'{x} is not equal to {y}')

# else:
#     print(f'condition false')


#Membership operators (not, not in) - Membership operators are used to test if a squence is presented in an object
b=17

numbers = [3,4,5,6,7,10]

# if b in numbers :
#     print(b in numbers)

# else :
#     print ('condition false')


# if b not in numbers :
#      print (f'Condition true ! {b} is not in numbers collections')

# else:
#     print ('condition false')         


#Identify operattors (is, is not) - compare the object , not if they are equal, but if they are actually the same object, with the same memory location:

# is 

# if x is y :
#     print (f'is should be true beacuse {x} equal to {y}')


# else :
#     print (f'conditionaly false {x} is not equal to {y}')


if x is not y :
    print (f'Conditionaly true beacuse {x} is not equal to {y}')

else:
    print (f'conditionaly false beacuse {x} is equl to {y}')