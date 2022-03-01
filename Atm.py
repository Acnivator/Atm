import os 
import shutil
import random
from sys import int_info
from unicodedata import name

from numpy import choose 

class atm:
    def __init__(self,pin,name):
        self.pin = pin
        self.name = name
        self.balance = 1000000

    def takeCash(self):
        cash = int(input("The amount of cash you want to withdraw: "))
        Amount = self.balance
        if(cash >= Amount):
            print("Your account does not have that much cash")
        else:
            self.balance = Amount - cash
            print(self.balance)
    
    def deposit(self):
        cash2 = int(input("Enter your amount you want to deposit: "))
        Amount = self.balance
        if(cash2 < 100):
            print("Enter more money because minimum amount is $100")        
        else:
            self.balance = Amount + cash2
            print(self.balance)


def main():
    pin = input("Enter your pin: ")
    name = input("Enter your name: ")
    atm1 = atm(pin,name)
    print("Select 1 for withdrowing and 2 fore depositing")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        atm1.takeCash()
    else:
        atm1.deposit()

main()

        
