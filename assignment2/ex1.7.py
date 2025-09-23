import numpy as np
import matplotlib.pyplot as plt

ts = np.array([float(l) for l in open("../sales_series.txt", "r")])

ma3 = np.convolve(ts, np.ones(3)/3, mode='valid')
ma7 = np.convolve(ts, np.ones(7)/7, mode='valid')

pred_3 = ma3[-1]  # forecast using last 3 weeks
pred_7 = ma7[-1]  # forecast using last 7 weeks

print(f"Next week prediction (3-week MA): {pred_3:.2f}")
print(f"Next week prediction (7-week MA): {pred_7:.2f}")

plt.figure(figsize=(10,6))
plt.plot(range(1, len(ts)+1), ts, label='Actual Sales', color='blue')
plt.plot(range(3, len(ts)+1), ma3, label='3-week Moving Average', color='orange')
plt.plot(range(7, len(ts)+1), ma7, label='7-week Moving Average', color='green')

# Mark forecast points
plt.scatter(len(ts)+1, pred_3, color='orange', marker='x', s=100, label='Next week (3-MA)')
plt.scatter(len(ts)+1, pred_7, color='green', marker='x', s=100, label='Next week (7-MA)')

plt.xlabel('Week')
plt.ylabel('Sales')
plt.title('Weekly Sales and Forecasts using Moving Averages')
plt.legend()
plt.grid(True)
plt.show()
