import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
tips = pd.read_csv("Tips.csv")

# Convert numeric columns
tips["total_bill"] = tips["total_bill"].astype(float)
tips["tip"] = tips["tip"].astype(float)

# Calculate tip percentage
tips["tip_percent"] = (tips["tip"] / tips["total_bill"]) * 100

# Analysis
total_revenue = tips["total_bill"].sum()
average_tip = tips["tip_percent"].mean()
best_day = tips.groupby("day")["tip_percent"].mean().idxmax()


# Print results
print("Total Revenue:", round(total_revenue, 2))
print("Average Tip Percentage:", round(average_tip, 2))
print("Best Tipping Day:", best_day)

# Save results to file
with open("results.txt", "w") as f:
    f.write(f"Total Revenue: ${total_revenue:.2f}\n")
    f.write(f"Average Tip Percentage: {average_tip:.2f}%\n")
    f.write(f"Best Tipping Day: {best_day}\n")

# Plot average tip percentage by day
tips.groupby("day")["tip_percent"].mean().plot(kind="bar")
plt.title("Average Tip Percentage by Day")
plt.xlabel("Day")
plt.ylabel("Tip Percentage")
plt.tight_layout()
plt.savefig("avg_tip_by_day.png")
plt.show()
