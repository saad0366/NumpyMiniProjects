import numpy as np
import matplotlib.pyplot as plt

# ----- Step 1: Setup -----
city = input("Enter city name: ")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
times = ["Morning", "Noon", "Evening", "Night"]

# ----- Step 2: Generate random temperature data (7x4) -----
# Temperatures between 15°C and 45°C
temps = np.random.randint(15, 46, size=(7, 4))

# ----- Step 3: Analyze -----
daily_avg = np.mean(temps, axis=1)
time_avg = np.mean(temps, axis=0)

hottest_day_index = np.argmax(daily_avg)
coldest_day_index = np.argmin(daily_avg)

# ----- Step 4: Display Results -----
print(f"\n🌤️ Weather Data for {city}\n")
print("Day   | Morning | Noon | Evening | Night | Avg Temp")
print("-" * 52)

for i in range(7):
    print(f"{days[i]:<5} | {temps[i,0]:<8} | {temps[i,1]:<4} | {temps[i,2]:<7} | {temps[i,3]:<5} | {daily_avg[i]:.1f}")

print("\n🧮 Average Temperature per Time of Day:")
for i, time in enumerate(times):
    print(f"  {time:<8}: {time_avg[i]:.1f}°C")

print(f"\n🔥 Hottest Day: {days[hottest_day_index]} ({daily_avg[hottest_day_index]:.1f}°C)")
print(f"❄️ Coldest Day: {days[coldest_day_index]} ({daily_avg[coldest_day_index]:.1f}°C)")

# ----- Step 5: Optional Visualization -----
plt.figure(figsize=(8, 4))
plt.plot(days, daily_avg, marker='o', color='orange', linewidth=2, label='Daily Avg Temp')
plt.title(f'Weekly Temperature Trend - {city}')
plt.xlabel('Day')
plt.ylabel('Average Temperature (°C)')
plt.grid(True)
plt.legend()
plt.show()
