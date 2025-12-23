class BankAccount:
    
    def __init__(self, account_holder: str, balance: float = 0) -> None:
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        self.balance += amount
    
    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print("Ошибка: Недостаточно средств на счете.")
        else:
            self.balance -= amount
    
    def get_balance(self) -> float:
        return self.balance