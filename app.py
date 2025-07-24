import random
import string
import streamlit as st


# Step 1: Create a class called Account and a constructor called when creating a new account
class Account:
    def __init__(self, account_holder, account_number, account_balance=0.0):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    def generate_account_number(self):
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return self.account_holder[:3].upper() + random_string

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount. Amount must be greater than zero."
        self.account_balance += amount
        return f"Deposit of KSH {amount:.2f} successful. New balance: KSH {self.account_balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount. Amount must be greater than zero."
        if amount > self.account_balance:
            return f"Insufficient funds. Available balance: KSH {self.account_balance:.2f}"
        self.account_balance -= amount
        return f"Withdrawal of KSH {amount:.2f} successful. New balance: KSH {self.account_balance:.2f}"

    def check_balance(self):
        return f"Account balance for {self.account_holder}: KSH {self.account_balance:.2f}"


# Initialize session state
if 'account_created' not in st.session_state:
    st.session_state.account_created = False

st.title("🏦 Kenya National Bank - Streamlit Banking App")

if not st.session_state.account_created:
    st.header("Create Your Account")
    name_input = st.text_input("Enter your name:")
    if st.button("Create Account") and name_input.strip():
        # Create account and store in session
        temp_account = Account(name_input, "")
        account_number = temp_account.generate_account_number()
        st.session_state.my_account = Account(name_input, account_number)
        st.session_state.account_created = True
        st.success("Account successfully created!")
        st.balloons()

# Display dashboard if account is created
if st.session_state.account_created:
    acc = st.session_state.my_account
    st.subheader(f"Welcome, {acc.account_holder} 👋")
    st.write(f"**Account Number:** `{acc.account_number}`")
    st.write(f"**Current Balance:** KSH {acc.account_balance:.2f}")

    st.divider()

    action = st.selectbox("Choose an action", ["Deposit", "Withdraw", "Check Balance"])

    if action == "Deposit":
        deposit_amount = st.number_input("Enter amount to deposit", min_value=0.0, format="%.2f")
        if st.button("Deposit"):
            result = acc.deposit(deposit_amount)
            st.info(result)

    elif action == "Withdraw":
        withdraw_amount = st.number_input("Enter amount to withdraw", min_value=0.0, format="%.2f")
        if st.button("Withdraw"):
            result = acc.withdraw(withdraw_amount)
            st.info(result)

    elif action == "Check Balance":
        if st.button("Show Balance"):
            st.success(acc.check_balance())

    if st.button("End Session"):
        st.session_state.clear()
        st.success("Session ended. Thank you for banking with us.")
