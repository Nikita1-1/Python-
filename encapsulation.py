

class BankAccount:

    def __init__(self, name, balance, passport, member_id):
        #double line - privat
        self.__name = name
        self.__balance = balance
        self.__passport = passport
        self._member_id = member_id
        # def print_public_data(self): public method that you can access to it no matter what
            #print(self.name, self.balance, self.passport)



    def print_protective_data(self):# this is a protective method meaning that you write this underline in case if this info should be printed oly inside the class
        print(self._member_id)# so if i create an object with this paramers and call it, it will give me error because parametr name, balance, passport in __init__ function are privat
        


    def print_privat_data(self):# in this case the information will be pri
        print(self.__name, self.__balance, self.__passport, self._member_id)# in this case i can access this parametrs in class function

bank1 = BankAccount('Bob', 1, 135,'AxJ49gL0')# use and protective and privat 
bank2 = BankAccount('Bob', 1, 13,'E0J492f28')#use only protective
bank1.print_privat_data()# getting access through the method because i cannot access to this directly like shown below
bank2.print_protective_data()
##print(bank1.__name)
##print(bank1.__balance)
##print(bank1.__passport)
## 
