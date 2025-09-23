import numpy as np
import matplotlib.pyplot as plt

ts = np.array([float(l.strip()) for l in open("../sales_series.txt", "r")])

def rmse(actual, predicted):
    return np.sqrt(np.mean((actual - predicted)**2))

errors = []
ma_series = {}
for w in range(1, 11):
    ma = np.convolve(ts, np.ones(w)/w, mode='valid')
    ma_series[w] = ma
    errors.append(rmse(ts[w-1:], ma))

errors_to_consider = errors[1:]
best_w = np.argmin(errors_to_consider) + 2
worst_w = np.argmax(errors_to_consider) + 2


print("RMSE by window size:")
for w, e in zip(range(1, 11), errors):
    print(f"{w}-week MA: {e:.2f}")
print(f"Lowest error: {best_w}-week MA, RMSE={errors[best_w-1]:.2f}")
print(f"Highest error: {worst_w}-week MA, RMSE={errors[worst_w-1]:.2f}")

plt.figure(figsize=(14,5))

# Plot1
plt.subplot(1,2,1)
plt.plot(range(1, 11), errors, marker='o', color='purple')
plt.xlabel('Moving Average Window Size (weeks)')
plt.ylabel('RMSE')
plt.title('Forecast Error vs Window Size')
plt.grid(True)

# Plot2
plt.subplot(1,2,2)

plt.plot(range(1, len(ts)+1), ts, label='Actual Sales', color='blue', linewidth=2, zorder=3)

best_ma_full = np.concatenate([np.full(best_w-1, np.nan), ma_series[best_w]])
plt.plot(range(1, len(ts)+1), best_ma_full, label=f'Best ({best_w}-week MA)', color='green', linewidth=2, zorder=2)

worst_ma_full = np.concatenate([np.full(worst_w-1, np.nan), ma_series[worst_w]])
plt.plot(range(1, len(ts)+1), worst_ma_full, label=f'Worst ({worst_w}-week MA)', color='red', linewidth=2, zorder=1)

plt.xlabel('Week')
plt.ylabel('Sales')
plt.title('Best vs Worst Moving Average Forecasts')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
