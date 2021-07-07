class User:
    def __init__(self, name):
        self.account_balance = 0
        self.name = name

    def make_deposit(self, amount):
        self.account_balance += amount
        print (f'{self.name} deposits: {amount}\n Your balance is: {self.account_balance}')
        return self

    def make_withdrawl(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print (f'{self.name} withdraws: {amount}\n Your balance is: {self.account_balance}')
            return self
        else:
            print(f'You attempted to witdraw {amount} but only have a balance of {self.account_balance}\n The transaction was cancelled')
            return self

    def disply_user_balance(self):
        print(f"{self.name}'s balance is {self.account_balance}")
        return self

    def transfer_money(self, amount, name):
        self.account_balance -= amount
        name.account_balance += amount
        print(f'{self.name} sent {name.name} {amount} \n {self.name} balance is {self.account_balance}\n {name.name} balance is {name.account_balance}' )

alex = User('Alex')
bob = User('Bob')
joe = User('Joe')

alex.make_deposit(500).make_deposit(1500).make_deposit(1000).make_withdrawl(500).disply_user_balance()

bob.make_deposit(500).make_deposit(500).make_withdrawl(1000).make_withdrawl(500).disply_user_balance()

joe.make_deposit(5000).make_withdrawl(1000).make_withdrawl(1000).make_withdrawl(500)

alex.transfer_money(500,joe)
