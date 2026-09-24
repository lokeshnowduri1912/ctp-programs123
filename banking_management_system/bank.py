from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BankAccount(ABC):
    account_number: str
    holder_name: str
    balance: float = 0.0

    @abstractmethod
    def account_type(self) -> str:
        pass

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance

    def display_details(self) -> None:
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Account Type: {self.account_type()}")
        print(f"Balance: ₹{self.balance:.2f}")


@dataclasss
class SavingsAccount(BankAccount):

    def account_type(self) -> str:
        return "Savings Account"


@dataclass
class CurrentAccount(BankAccount):

    overdraft_limit: float = 5000.0

    def account_type(self) -> str:
        return "Current Account"

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Withdrawal exceeds overdraft limit")
        self.balance -= amount