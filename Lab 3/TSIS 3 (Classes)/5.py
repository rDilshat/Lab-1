class bankaccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if(amount > 0):
            self.balance+=amount
            print("Deposit balance:", self.balance)
        else:
            print("Deposit amount must be higher than 0")
    def Withdrawals(self, amount):
        if(amount > 0):
            if(amount <= self.balance):
                self.balance-=amount
                print("Current balance:", self.balance)
            else:
                print("Withdrawals mustn't be higher than balance")
        else:
            print("Withdrawals must be higher than 0")

account = bankaccount(str(input()))
account.deposit(int(input()))
account.Withdrawals(int(input()))
account.Withdrawals(int(input()))
print(account.owner, "your current balance:", account.balance)