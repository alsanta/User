class User:
    def __init__(self, name):
        self.account_balance = 0
        self.name = name
    def make_deposit(self, amount):
        self.account_balance += amount
        print (f'{self.name} deposits: {amount}\n Your balance is: {self.account_balance}')

    def make_withdrawl(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print (f'{self.name} withdraws: {amount}\n Your balance is: {self.account_balance}')
        else:
            print(f'You attempted to witdraw {amount} but only have a balance of {self.account_balance}\n The transaction was cancelled')

    def disply_user_balance(self):
        print(f'{self.name} balance is {self.account_balance}')

    def transfer_money(self, amount, name):
        self.account_balance -= amount
        name.account_balance += amount
        print(f'{self.name} sent {name.name} {amount} \n {self.name} balance is {self.account_balance}\n {name.name} balance is {name.account_balance}' )

alex = User('Alex')
bob = User('Bob')
joe = User('Joe')

alex.make_deposit(500)
alex.make_deposit(1500)
alex.make_deposit(1000)
alex.make_withdrawl(500)

bob.make_deposit(500)
bob.make_deposit(500)
bob.make_withdrawl(1000)
bob.make_withdrawl(500)

joe.make_deposit(5000)
joe.make_withdrawl(1000)
joe.make_withdrawl(1000)
joe.make_withdrawl(500)

alex.transfer_money(500,joe)
