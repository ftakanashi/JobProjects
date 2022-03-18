#!/usr/bin/env python
from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.cash = {}
        for i, num in enumerate(balance):
            self.cash[i+1] = num

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        cash = self.cash
        if account1 in cash and account2 in cash and cash[account1] >= money:
            cash[account1] -= money
            cash[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.cash:
            self.cash[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.cash and self.cash[account] >= money:
            self.cash[account] -= money
            return True
        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)