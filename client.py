from random import randint


class Client:

    # {account_number: *****, name: "Anton", holdings: 500}
    account = {}

    def __init__(self, name, deposit):
        self.account['account_number'] = randint(10000, 99999)
        self.account['name'] = name
        self.account['holdings'] = deposit

    def withdraw(self, amount):
        if self.account['holdings'] >= amount:
            self.account['holdings'] -= amount
            print("The sum of {} has been withdrawn from your account balance.".format(amount))
            self.balance()
        else:
            print()
            print("Not enough funds!")

    def deposit(self, amount):
        self.account['holdings'] += amount
        print("The sum of {} has been added to your account balance.".format(amount))

    def balance(self):
        print()
        print("Your current account balance is {}".format(self.account['holdings']))
