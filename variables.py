# A variable is a container for a value , which can be of various types

'''

this is a multiline comment
ordocstring (used to define a function purpose)
can be single or double quotes
'''


"""
Variable Rules:
- Variable names are case sensitive (name and name are different variables)
- Must start with a letter or an underscore
-can have number but can not start with one
"""

'''
Variables types
'''

# x= 1 #int 
# y = 2.5 #float
# name= 'Miraz' #string
# is_cool = True #bool

#Multiple Assigment

x,y, name, is_cool = (1, 2.5, 'Miraz', True)

print (x,y,name, is_cool)


#Basic math

a=x+y

print (a)

#Casting

x= str(y)
print(x)
y= init(y)

#Check Type 
print (type(is_cool))

print (type(y))
