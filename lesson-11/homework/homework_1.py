class Bank():
    def __init__(self, account = 0):
        self.account = account
    def deposit(self):
        x = int(input('\nEnter the amount of deposit: \n'))
        self.account = x + self.account
        print("\nDeposit Completed Successfully.")
    def withdrawal(self):
        y = int(input('\nEnter the amount of money you want to withdraw: \n'))
        if self.account >= y:
            self.account = self.account - y
            print("\nWithdrawal Completed Successfully.")
        else:
            print('\nTransaction Failed: Insufficient Funds')
    def check(self):
        print(f"\nYour balance: {self.account}")

def main():
    b = Bank()
    while True:
        print('\nEnter 1 to put deposit')
        print('Enter 2 to withdraw money')
        print('Enter 3 to see your balance')
        print('Enter 4 to quit')

        command = int(input('Enter your command: '))
        if command == 1:
            b.deposit()
        elif command == 2:
            b.withdrawal()
        elif command == 3:
            b.check()
        elif command == 4:
            break

main()
