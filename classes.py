# A Class is like a blueprint for creating objects. An object
# has properties and methods(functions) associate with it. almost everything in python is an object

#Create class
class User:

    #Constructor
    def __init__(self, name , email, age):
        self.name =name
        self.email = email
        self.age = age  



  #method
    def greeting(self):
        return(f'My name is {self.name} and I am {self.age}')

    # def has_birthday(self):
    #    self.age+=1

#Customer Class

class Customer(User):
     def __init__(self,name, email, age):
            self.name =name
            self.email = email
            self.age = age
            self.balance= 0
     def set_balance(self, balance):
           self.balance = balance
     def greeting(self):
        return(f'My name is {self.name} and my balance is {self.balance} and my age is {self.age}')



# Init user object

jhon = User('Jhon doe', 'jhon@gmail.co', 37)
doe = User('doe', 'doe@gmail.com',23)

 #Init Customer
bablu = Customer('the bablu', 'bablu@gmail.com', 45)
bablu.set_balance(500)

# print(bablu.balance)

#Edit property
jhon.age= 40

# call method

# print (doe.greeting())



print(bablu.greeting())
