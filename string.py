#String in python are surrounded by either single or double quotation marks
#. lets  look at  string  formation and some string methods

name = 'Miraz'
age=45;

#contacting

#print('Hello I am' + name + 'and I am' + str(age))

#string formating

#Arguments by pisition
#print ('{}, {}, {}'.format('a','b','c'))
#print('{1}, {2}, {0}'.format('a','b','c'))

#Arguments By Name

#print('My name is {name} and I am{age}'.format(name='Miraz', age=45))

# F-string(only in 3.6+)

# print(f'My name is{name} and I am{age}')
  b = 'hello there world'
  #Capitalize first letter

print(s.Capitalize())

#make all lower
print(s.lower())

# make all upper
print(s.upper())

#swap case

print (s.swapcase())

# get length

print(len(s))

#replace
print(s.replace('world', 'everyone'))

#Starts with

print(s.startswith('hello'))

#end width 

print(s.endwith('d'))


#find position
print(s.find('r'))


#split into a list
print(s.split())

#is all alphanumeric

print (is.isalnum())

#is all numeric
print(s.isnumeric())