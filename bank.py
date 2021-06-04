class Account:
    def __init__(self,accountType,pin,name,phoneNumber):
        self.accountType=accountType
        self.balance=0 
        self.pin=pin
        self.name=name
        self.phoneNumber=phoneNumber
    def deposit_cash(self,amount):
        if amount >0:
          self.balance+=amount
        # return f"Dear {self.name} you have deposited {amount} and your new balance is {self.balance}"
          return  f"he amount is greater than zero"
        else:
            self.balance+=amount
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
