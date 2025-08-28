# chapter_01.py - Implementation of financial contracts concepts from Natenberg
import math

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