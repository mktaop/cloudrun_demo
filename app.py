import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_mortgage(amount, interest_rate, years):
    """
    Calculates monthly payment for a fixed-rate mortgage.
    """
    interest_rate = interest_rate / 100 / 12
    months = years * 12
    monthly_payment = (amount * interest_rate * ((1 + interest_rate) ** months)) / (((1 + interest_rate) ** months) - 1)
    return monthly_payment

def generate_graph(amount, interest_rate, years):
    """
    Generates a graph showing the breakdown between principal and interest payments over the term of the mortgage.
    """
    interest_rate = interest_rate / 100 / 12
    months = years * 12
    balance = amount
    principal_payments = []
    interest_payments = []
    for i in range(months):
        interest_payment = balance * interest_rate
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment
        principal_payments.append(principal_payment)
        interest_payments.append(interest_payment)
    plt.plot(principal_payments, label='Principal')
    plt.plot(interest_payments, label='Interest')
    plt.xlabel('Month')
    plt.ylabel('Payment')
    plt.title('Breakdown of Monthly Payment')
    plt.legend()
    return plt

st.title('Mortgage Calculator')

# User input
amount = st.slider('Loan Amount', 1000, 1000000, 100000, step=1000)
interest_rate = st.slider('Interest Rate', 0.1, 20.0, 3.0, step=0.1)
years = st.slider('Number of Years', 1, 30, 15)

# Calculate monthly payment
monthly_payment = calculate_mortgage(amount, interest_rate, years)
st.write(f'Monthly Payment: ${monthly_payment:.2f}')



# Generate monthly breakdown graph
interest_rate = interest_rate / 100 / 12
months = years * 12
balance = amount
principal_payments = []
interest_payments = []
for i in range(months):
    interest_payment = balance * interest_rate
    principal_payment = monthly_payment - interest_payment
    balance -= principal_payment
    principal_payments.append(principal_payment)
    interest_payments.append(interest_payment)
plt.figure()
plt.plot(principal_payments, label='Principal')
plt.plot(interest_payments, label='Interest')
plt.xlabel('Month')
plt.ylabel('Payment')
plt.title('Monthly Breakdown of Payment')
plt.legend()
st.pyplot(plt)
