import streamlit as st
import random
import string

class Account:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.account_balance += amount
        return f"You've successfully deposited {amount} ksh."

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return f"You've successfully withdrawn {amount} ksh."
        return "You have insufficient balance."

    def check_balance(self):
        return f"Your account balance is {self.account_balance} ksh."

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: {self.account_balance} ksh"

    def generate_account_number(self, account_holder: str) -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Initialize session state for accounts
if 'accounts' not in st.session_state:
    st.session_state.accounts = {}

def main():
    st.title("Standard Chartered Bank")
    st.write("Welcome to Standard Chartered Bank!")

    menu = st.sidebar.selectbox("Menu", ["Create Account", "Manage Account"])

    if menu == "Create Account":
        account_holder = st.text_input("Enter account holder name")
        if st.button("Create Account") and account_holder:
            account_number = Account("", 0, "").generate_account_number(account_holder)
            st.session_state.accounts[account_holder] = Account(account_number, 0, account_holder)
            st.success(f"Account created for {account_holder} with account number {account_number}")

    elif menu == "Manage Account":
        if not st.session_state.accounts:
            st.warning("Please create an account first.")
        else:
            selected_holder = st.selectbox("Select an account", list(st.session_state.accounts.keys()))
            selected_acc = st.session_state.accounts[selected_holder]
            st.write(selected_acc)

            operation = st.selectbox("Account Operations", ["Deposit", "Withdraw", "Check Balance"])
            
            if operation == "Deposit":
                amount = st.number_input("Enter amount to deposit", min_value=0.0)
                if st.button("Deposit") and amount > 0:
                    result = selected_acc.deposit(amount)
                    st.success(result)

            elif operation == "Withdraw":
                amount = st.number_input("Enter amount to withdraw", min_value=0.0)
                if st.button("Withdraw") and amount > 0:
                    result = selected_acc.withdraw(amount)
                    st.write(result)

            elif operation == "Check Balance":
                if st.button("Check Balance"):
                    st.write(selected_acc.check_balance())

if __name__ == "__main__":
    main()
