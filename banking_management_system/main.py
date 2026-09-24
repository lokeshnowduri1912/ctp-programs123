from bank import BankAccount, SavingsAccount, CurrentAccount


def show_account(account: BankAccount) -> None:
    print()
    account.display_details()


def main() -> None:
    savings: SavingsAccount = SavingsAccount(
        account_number="SB1001",
        holder_name="Rohith",
        balance=10000.0
    )

    current: CurrentAccount = CurrentAccount(
        account_number="CA1001",
        holder_name="Rahul",
        balance=5000.0
    )

    savings.deposit(2000.0)
    savings.withdraw(1500.0)

    current.deposit(3000.0)
    current.withdraw(10000.0)

    show_account(savings)
    show_account(current)


if __name__ == "__main__":
    main()