from cProfile import label
import math
import time
from turtle import color

def calulate_notional_value(quantity, price_per_unit):
    """
    Calculate the notional value of a contract.
    
    Parameters:
    quantity (int): The number of units (e.g. shares)
    price_per_unit (float): The price per unit

    Returns:
    float: The notional value of the contract
    """
    return quantity * price_per_unit

def forward_price(spot_price, risk_free_rate, time_to_maturity):
    """
    Calculate the forward price using continuous compouding.
    
    Parameters:
    spot_price (float): The current spot price of the asset
    risk_free_rate (float): The annualized risk-free interest rate (as a decimal)
    time_to_maturity (float): The time to maturity in years

    Returns:
    float: The forward price of the asset
    """
    return spot_price * math.exp(risk_free_rate * time_to_maturity)


# Examples:

spot_price = 100  # Current spot price
risk_free_rate = 0.05  # 5% annual risk-free rate
time_to_maturity = 1  # 1 year to maturity
quantity = 10  # Number of units

notional_value = calulate_notional_value(quantity, spot_price)
fwd_price_value = forward_price(spot_price, risk_free_rate, time_to_maturity)

print(f"Notional Value: ${notional_value:.2f}")
print(f"Forward Price: ${fwd_price_value:.2f}")

# Exercise 1: Test different parameters scenarios
test_cases = [
    {"spot_price": 150, "risk_free_rate": 0.03, "time_to_maturity": 0.5, "quantity": 20},
    {"spot_price": 200, "risk_free_rate": 0.07, "time_to_maturity": 2, "quantity": 5},
    {"spot_price": 50, "risk_free_rate": 0.04, "time_to_maturity": 1.5, "quantity": 100},
]   

print("\nTesting different scenarios:")
for case in test_cases:
    notional_value = calulate_notional_value(case["quantity"], case["spot_price"])
    fwd_price_value = forward_price(case["spot_price"], case["risk_free_rate"], case["time_to_maturity"])
    print(f"Spot Price: ${case['spot_price']}, Risk-Free Rate: {case['risk_free_rate']*100}%, Time to Maturity: {case['time_to_maturity']} years, Quantity: {case['quantity']}")
    print(f"  Notional Value: ${notional_value:.2f}")
    print(f"  Forward Price: ${fwd_price_value:.2f}\n")
    time.sleep(1)  # Pause for readability

# Exercise 2: Visualize forward price sensitivity to time
import matplotlib.pyplot as plt
time_value = [t / 12 for t in range(0, 25)]  # Time from 0 to 2 years in months
fwd_prices = [forward_price(spot_price, risk_free_rate, t) for t in time_value]
plt.plot(time_value, fwd_prices, label='Forward Price over Time', color='blue')
plt.title('Forward Price Sensitivity to Time')
plt.xlabel('Time to Maturity (years)')
plt.ylabel('Forward Price ($)')
plt.legend()
plt.grid(True)
plt.show()


