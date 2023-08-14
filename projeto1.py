from datetime import datetime, timedelta

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.daily_withdrawal_count = 0
        self.last_withdrawal_date = None

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.deposits.append(amount)
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance and self.daily_withdrawal_count < 3 and amount <= 500:
            self.balance -= amount
            self.withdrawals.append(amount)
            self.daily_withdrawal_count += 1
            self.last_withdrawal_date = datetime.now()
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def get_statement(self):
        if not self.deposits and not self.withdrawals:
            return "Não foram realizadas movimentações."
        
        statement = "Extrato:\n"
        for deposit in self.deposits:
            statement += f"Depósito: R$ {deposit:.2f}\n"
        for withdrawal in self.withdrawals:
            statement += f"Saque: R$ {withdrawal:.2f}\n"
        statement += f"Saldo Atual: R$ {self.balance:.2f}"
        return statement

    def reset_daily_withdrawal(self):
        if self.last_withdrawal_date is not None and datetime.now().date() > self.last_withdrawal_date.date():
            self.daily_withdrawal_count = 0

# Exemplo de uso
account = BankAccount()
account.deposit(1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(300)
account.withdraw(150)
account.withdraw(1000)  # Isso deve falhar devido ao limite diário
print(account.get_statement())
account.reset_daily_withdrawal()
