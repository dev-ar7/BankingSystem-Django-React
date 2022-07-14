from .models import User, Account
from decimal import Decimal


class BankAccountTransactions():


    def __init__(self, account, amount):
        try:
            self.amount = Decimal(amount)
            if self.amount <= 10:
                raise ValueError('Insufficient Balance In Your Account')
            if self.amount > 99999999999.99:
                raise ValueError('Maximum Value Exceeded')
        except:
            raise ValueError('Bad Input Of Amount')

        self.account = account
        if not isinstance(account, Account):
            raise ValueError('')


    def deposit_amount(self):
        account = self.account
        amount = self.amount
        new_balance = account.current_balance + amount
        if new_balance > 99999999999.99:
            raise ValueError('Max Value Exceeded')
        account.current_balance += amount
        account.save()
        return True


    def withdraw_amount(self):
        account = self.account
        amount = self.amount
        current_balance = account.current_balance

        if current_balance >= amount:
            account.current_balance -= amount
            account.save()
            return True
        return False