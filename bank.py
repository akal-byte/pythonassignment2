from datetime import datetime
class Account:
    def __init__(self,accountType,pin,name,phoneNumber):
        self.accountType=accountType
        self.balance=0 
        self.pin=pin
        self.name=name
        self.phoneNumber=phoneNumber
        self.transactions=[]
    def deposit_cash(self,amount):
        if amount < 0:
          self.balance+=amount
        # return f"Dear {self.name} you have deposited {amount} and your new balance is {self.balance}"
          return  f"The amount is greater than zero"
        else:
            self.balance+=amount
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"deposit"}
            self.transactions.append(transaction)
            return f" you have deposited {amount} and your balance is {self.balance}"
    def show_balance(self):
        return self.balance
    def withdraw_cash(self,amount):
        if amount <=0:
            return f" The amount must be greater than zero"
        elif amount > self.balance:
             return f" The amount must be less than the balance"
        else:
            self.balance-=amount
            return f"your balance is {self.balance} after withdrawing {amount} " 
    def borrow(self,loan,loanLimit):
        # loanLimit=7000
        if self.balance <=loanLimit:
            return f"Dear {self.name} of account {self.accountType} and phone {self.phoneNumber} your loan limit is {loanLimit} "
        elif loan < 0:
            return f"you qualify for a loan."
        else:
            self.balance+=loan
            return f"Dear {self.name} of account {self.accountType} and phone {self.phoneNumber} your loan limit is {loanLimit} and you new balance is {self.balance}"
    #handling time
    def get_time(self):
        for transaction in self.transactions:
             narration=transaction["narration"]
             amount=transaction["amount"]
             balance=transaction["balance"]
             time=transaction["time"]
             print(f"{time.strftime('%D')} your narration is {narration} and transaction amount is {amount}") 


    def loan_repayment(self,amount):

        if amount>=self.loan:
            return f"you have repaid your loan of amount {amount},your new balance{amount-self.loan}"
        elif amount<self.loan:
            return f"you have a pending loan of { self.loan- amount}. Please repay"
        else:
            return f"you do not have a pending loan"   