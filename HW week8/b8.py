class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, x):
        self.balance += x
    def withdraw(self, x):
        if x <= self.balance:
            self.balance -= x
    def __str__(self):
        return f"{self.owner}: {self.balance}"
owner, initial_balance = input().split()
initial_balance = int(initial_balance)
account = BankAccount(owner, initial_balance)
n = int(input())
for _ in range(n):
    cmd, x = input().split()
    x = int(x)
    if cmd == "DEPOSIT":
        account.deposit(x)
    elif cmd == "WITHDRAW":
        account.withdraw(x)
    else:
        print("INVALID COMMAND")
print(f"{account.balance:.2f}")