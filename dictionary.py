# A Dictionaru is collection which is unorderd , changeable and indexed no duplicate members,

# simple dict

person = {
    'first_name':'john',
    'last_name':'Doe',
    'age':30,
    'phone':345
}

# print(person)



#Using a constructor

# personConst = dict(first_name='Miraz', last_name='Karim', age=34)

# print (personConst)


#Acccess value

# print (person['first_name'])

# print(person.get('last_name'))


#Add key / value

# person['phone'] = '555-565-5454'

# print(person)

#Get items

# print(person.items())

#Get keys

# print(person.keys())


#Make copy 

# person2 = person.copy()

# person2['city'] = 'Boston'

# print(person2)

#Remove item 

# del(person['age'])
# person.pop('phone')
# person.clear()

# print(person)

#list of dic

people = [
    {'name':'Martha', 'age':40},
    {'name':'Bob', 'age':20}
]

# access list of dic
print(people[1]['name'])


