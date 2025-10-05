import numpy as np
import matplotlib.pyplot as plt

# ----- Step 1: Setup -----
days = 30
initial_price = 100

# ----- Step 2: Generate random daily changes -----
# Random integers between -5 and 5 for each day
daily_changes = np.random.randint(-5, 6, size=days)

# ----- Step 3: Simulate stock prices -----
# Initialize prices array
prices = np.zeros(days, dtype=float)
prices[0] = initial_price

# Update price each day (based on previous day)
for i in range(1, days):
    prices[i] = prices[i - 1] + daily_changes[i]
    
# Optional: Prevent negative prices
prices = np.clip(prices, 1, None)

# ----- Step 4: Analyze data -----
average_price = np.mean(prices)
max_price = np.max(prices)
min_price = np.min(prices)

# ----- Step 5: Display results -----
print("📊 Stock Price Simulator Results\n")
print(f"Initial Price: {initial_price}")
print(f"Average Price over {days} days: {average_price:.2f}")
print(f"Highest Price: {max_price:.2f}")
print(f"Lowest Price: {min_price:.2f}\n")

print("📈 Price Trend:")
print(np.round(prices, 2))

# ----- Step 6: (Optional) Visualize trend -----
plt.figure(figsize=(8, 4))
plt.plot(prices, marker='o', color='blue', linewidth=2, label='Stock Price')
plt.title('Stock Price Simulation (30 Days)')
plt.xlabel('Day')
plt.ylabel('Price')
plt.grid(True)
plt.legend()
plt.show()
