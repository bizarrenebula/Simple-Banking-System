import random


class Client:

    def __init__(self, name, deposit):
        self.name = name
        self.savings = deposit
        self.acc_number = random.randint(10000, 99999)

    def withdraw(self, amount):
        if self.savings >= amount:
            self.savings -= amount
            print("The sum of {} has been withdrawn from your account balance.".format(amount))
        else:
            print("Not enough funds!")

    def deposit(self, amount):
        self.savings += amount
        print("The sum of {} has been added to your account balance.".format(amount))

    def balance(self):
        print("Your current account balance is {}".format(self.savings))
