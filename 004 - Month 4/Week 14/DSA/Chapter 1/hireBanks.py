#! python3
#       hireBanks.py | dsa chapter 1 exercise
#       class hierarchy for bank accounts(money, people, bank)
#       A little lazy, I just sort of plopped it all in an array of dictionary values. Just another way to solve it

import sys


# bank main
class Bank:
    def __init__(self):
        pass


class Money:
    def __init__(self):
        self.accounts = [{"Customer": "Alice", "Balance": 100}, {"Customer": "Bob", "Balance": 200},
                         {"Customer": "Carol", "Balance": 300}, {"Customer": "Dave", "Balance": 400}]

    def balance(self):
        for account in self.accounts:
            print(f"Customer: {account['Customer']}, Balance: {account['Balance']}")


# menu
def Menu():
    our_money = Money()
    our_money.balance()


if __name__ == "__main__":
    Menu()
