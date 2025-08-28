# chapter_01.py - Implementation of financial contracts concepts from Natenberg
import math
import matplotlib.pyplot as plt

# Function to calculate notional value
def calculate_notional_value(quantity, price):
    """
    Calculate the notional value of a contract.
    quantity: number of units (e.g., shares)
    price: price per unit
    """
    return quantity * price

# Forward price function based on Natenberg's no-arbitrage principle
def forward_price(S, r, T):
    """
    Calculate forward price with continuous compounding (no dividends).
    S: spot price
    r: risk-free rate
    T: time to maturity (years)
    """
    return S * math.exp(r * T)

# Example parameters from Chapter 1 context
spot_price = 100    # Spot price ($)
risk_free_rate = 0.05  # 5% risk-free rate
time_to_maturity = 1  # 1 year
contract_quantity = 100  # Number of shares

# Calculate and print results
notional_value = calculate_notional_value(contract_quantity, spot_price)
forward_price_value = forward_price(spot_price, risk_free_rate, time_to_maturity)
print(f"Notional Value: ${notional_value:.2f}")
print(f"Forward Price: ${forward_price_value:.2f}")

# Exercise 1: Modify Parameters
test_cases = [
    {"S": 50, "r": 0.03, "T": 0.5, "quantity": 200},  # 6 months, 200 shares
    {"S": 200, "r": 0.06, "T": 2, "quantity": 50}      # 2 years, 50 shares
]
print("\nTest Cases:")
for case in test_cases:
    notional = calculate_notional_value(case["quantity"], case["S"])
    forward = forward_price(case["S"], case["r"], case["T"])
    print(f"Case - Notional: ${notional:.2f}, Forward: ${forward:.2f}")

# Exercise 2: Plot sensitivity to time
T_values = [t / 12 for t in range(1, 25)]  # Months to years (1 to 24 months)
F_values = [forward_price(spot_price, risk_free_rate, t) for t in T_values]
plt.plot(T_values, F_values, label='Forward Price')
plt.xlabel('Time to Maturity (Years)')
plt.ylabel('Forward Price')
plt.title('Forward Price vs. Time')
plt.legend()
plt.grid(True)
plt.show()

# Comments
# Forward price increases with time due to interest cost
# Notional value scales with quantity and price, key for contract sizing