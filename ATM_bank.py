class Account:
    def __init__(self, cardNumber, pin, balance, withdrawalAmount, accountType):
        self.cardNumber = cardNumber
        self.pin = pin
        self.balance = balance
        self.withdrawalAmount = withdrawalAmount
        self.accountType = accountType

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount <= self.balance:
            self.balance -= withdrawalAmount
            self.withdrawalAmount = withdrawalAmount
            return True
        else:
            return False

class ATM:
    def __init__(self, branch_name, accountList):
        self.branch_name = branch_name
        self.accountList = accountList

    def validate_account(self, cardNumber, pin, withdrawalAmount):
        for account in self.accountList:
            if account.cardNumber == cardNumber and account.pin == pin:
                if account.withdraw(withdrawalAmount):
                    return account
                else:
                    return None
        return None

    def filter_accounts_by_type(self, accountType):
        filtered_accounts = {}
        for account in self.accountList:
            if account.accountType.lower() == accountType.lower():
                filtered_accounts[account.cardNumber] = account.balance
        if not filtered_accounts:
            return None
        return filtered_accounts


# Main program
if __name__ == "__main__":
    num_accounts = int(input())
    account_list = []
    for _ in range(num_accounts):
        cardNumber = int(input())
        pin = int(input())
        balance = float(input())
        withdrawalAmount = float(input())
        accountType = input()
        account = Account(cardNumber, pin, balance, withdrawalAmount, accountType)
        account_list.append(account)

    branch_name = input()
    atm = ATM(branch_name, account_list)

    card_number = int(input())
    pin = int(input())
    withdrawal_amount = float(input())

    # Attempt to withdraw money from the account and update the balance
    account = atm.validate_account(card_number, pin, withdrawal_amount)
    if account:
        print(f"{account.cardNumber} {account.balance:.1f} {account.withdrawalAmount:.1f}")
    else:
        print("No account Exists")

    account_type_to_search = input()
    accounts_by_type = atm.filter_accounts_by_type(account_type_to_search)
    if accounts_by_type:
        for card_number, balance in sorted(accounts_by_type.items(), key=lambda x: x[1]):
            print(f"{card_number} {balance:.1f}")
    else:
        print("No match Found")
