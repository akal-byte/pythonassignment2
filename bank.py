from datetime import datetime
from typing import ClassVar
class Account:
    def __init__(self,accountType,pin,name,phoneNumber,loan):
        self.accountType=accountType
        self.balance=0 
        self.pin=pin
        self.name=name
        self.phoneNumber=phoneNumber
        self.transactions=[]
        self.loan=loan
    def deposit_cash(self,amount):
        try:
            12+amount
        except TypeError:
            return "please enter amount in figures"
        if amount < 0:
          self.balance+=amount
          return  f"The amount is greater than zero"
        else:
            self.balance+=amount
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"deposit"}
            self.transactions.append(transaction)
            return f" you have deposited {amount} and your balance is {self.balance}"
    def show_balance(self):
        return self.balance
    def withdraw_cash(self,amount):
        try:
            12+amount
        except TypeError:
            return f"The amount must be in figures"
        if amount <=0:
            return f" The amount must be greater than zero"
        elif amount > self.balance:
             return f" The amount must be less than the balance"
        else:
            self.balance-=amount
            return f"your balance is {self.balance} after withdrawing {amount} " 
    def borrow(self,loanLimit):
        loanLimit=7000
        if self.balance <=loanLimit:
            return f"Dear {self.name} of account {self.accountType} and phone {self.phoneNumber} your loan limit is {loanLimit} "
        elif self.loan < 0:
            return f"you qualify for a loan."
        else:
            self.balance+=self.loan
            return f"Dear {self.name} of account {self.accountType} and phone {self.phoneNumber} your loan limit is {loanLimit} and you new balance is {self.balance}"
    #handling time
    def get_time(self):
        for transaction in self.transactions:
             narration=transaction["narration"]
             amount=transaction["amount"]
             self.balance=transaction["balance"]
             time=transaction["time"]
             print(f"{time.strftime('%D')} your narration is {narration} and transaction amount is {amount}") 


    def loan_repayment(self,amount):
        if amount>=self.loan:
            return f"you have repaid your loan of amount {amount}.Your new balance{amount-self.loan}"
        elif amount<self.loan:
            return f"you have a pending loan of { self.loan- amount}. Please repay"
        else:
            return f"you do not have a pending loan"
    def transfer(self,amount,account):
        try:
         amount+1
        except TypeError:
         return f" amount must be in figures"
        # if amount < self.balance - trans
        fee=amount*0.05
        if amount+fee>=self.balance:
            return f"you do not have enough balance to proceed with the transaction. You need {amount+fee}"
        else:
            self.balance-=amount+fee
            account.deposit_cash(amount)
            return f"your new balance is {self.balance}"


class MobileMoney(Account):
    def __init__(self,accountType,pin,name,phoneNumber,loan,service_provider):
      super().__init__(accountType,pin,name,phoneNumber,loan)
      self.serviceprovider= service_provider
      self.limit=300000
    def buy_airtime(self,amount):
        if amount>self.limit:
            return " please select a lower amount to transact with as your limit is {self.limit} "
        else:
           return f"Dear {self.name} you have bought airtime worth {amount} and your balance is {self.balance-amount}"



