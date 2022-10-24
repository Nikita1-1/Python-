

class Person:
    # to avoid same code every time, it is correct to write this
    # __init__ is using when we need to create a new object class Person and take parametrs as:
    #self means it takes parametrs from new object as: name etc
    def __init__(self, name, age, last_name):
        self.name = name
        self.age = age
        self.last_name = last_name
    def print_person(self):
        print('First_Name: {}, age: {}, last_name: {}'.format(self.name, self.age, self.last_name))



p1 = Person('Elon', 23, 'Musk')


p1.print_person()

              


#inheritance

class User:
    name = 'No name'
    email = ''
    password ='123qwerty'
    account_number = 0
    
#class employee inherint attributes from User class + its own parametrs

class Employee(User):
    base_pay = 12.00
    postion = ''

class Customer(User):
    mailing_address = ''
    mailing_list = ''
