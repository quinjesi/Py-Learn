from tkinter import *

root = Tk()
root.title('StarPay')

title_label = Label(root, text='Welcome to StarPay', bg="#3B061F", fg='black', font=('Verdana', 16, 'bold'))
title_label.grid(row=0, column=1, columnspan=5, padx=10, pady=10)


message_label = Label(root, text='', fg='black', font=('Verdana', 12))
message_label.grid(row=1, column=1, columnspan=5, padx=10, pady=10)

class BankSystemGUI():
    def __init__(self, master):
        self.balance = 250000
        self.entry = Entry(master, font=('Verdana', 16, 'bold'), width=10)
        self.entry.grid(row=2, column=1, columnspan=5, padx=10, pady=10)
    
    def deposit(self):
        try:
            deposit_input = int(self.entry.get())
            self.balance += deposit_input
            message_label.config(text=f"Deposit successful. New balance: ₦{self.balance}")
        except ValueError:
            message_label.config(text="Invalid input. Please enter a valid amount.")

    def withdraw(self):
        try:
            withdraw_input = int(self.entry.get())
            if withdraw_input > self.balance:
                message_label.config(text="Insufficient funds.")
            else:
                self.balance -= withdraw_input
                message_label.config(text=f"Withdrawal successful. New balance: ₦{self.balance}")
        except ValueError:
            message_label.config(text="Invalid input. Please enter a valid amount.")

app = BankSystemGUI(root)


deposit_button = Button(root, text='Deposit', command=app.deposit, bg='#3B061F', fg='white', font=('Verdana', 16, 'bold'))
withdraw_button = Button(root, text='Withdraw', command=app.withdraw, bg='#3B061F', fg='white', font=('Verdana', 16, 'bold'))

deposit_button.grid(row=3, column=1, columnspan=1, padx=10, pady=10)
withdraw_button.grid(row=3, column=2, columnspan=1, padx=10, pady=10)

root.mainloop()


