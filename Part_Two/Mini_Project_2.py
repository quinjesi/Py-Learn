class BankSystem():
    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        confirm_deposit = input("Do you want to deposit money? (yes/no) \n: ").lower()
        if (confirm_deposit == 'yes'):
            deposit_amount = eval(input("Enter the amount you want to deposit: \n: "))
            self.balance += deposit_amount
        else:
            print("Deposit cancelled.")

    def withdraw(self):
        confirm_withdraw = input("Do you want to withdraw money? (yes/no) \n: ").lower()
        if (confirm_withdraw == 'yes'):
            withdraw_amount = eval(input("Enter the amount you want to withdraw: \n: "))
            if withdraw_amount > self.balance:
                confirm_overdraft = input("Insufficient balance.\n Would you like to request an overdraft? (yes/no) \n: ").lower()
                if confirm_overdraft == 'yes':
                    print('Your request is being reviewed and an email will be sent to you soon.')
                else:
                    print('Operation cancelled.')
            else:
                self.balance -= withdraw_amount
                print(f"Withdrawal successful. New balance: {self.balance}")
        else:
            print("Withdrawal cancelled.")


bank = BankSystem(250000)
bank.deposit()
bank.withdraw()