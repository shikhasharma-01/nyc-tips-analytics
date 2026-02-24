import pandas as pd
import matplotlib.pyplot as plt


tips = pd.read_csv("Tips.csv")


tips["total_bill"] = tips["total_bill"].astype(float)
tips["tip"] = tips["tip"].astype(float)


tips["tip_percent"] = (tips["tip"] / tips["total_bill"]) * 100

total_revenue = tips["total_bill"].sum()
average_tip = tips["tip_percent"].mean()
best_day = tips.groupby("day")["tip_percent"].mean().idxmax()


print("Total Revenue:", round(total_revenue, 2))
print("Average Tip Percentage:", round(average_tip, 2))
print("Best Tipping Day:", best_day)


with open("results.txt", "w") as f:
    f.write(f"Total Revenue: ${total_revenue:.2f}\n")
    f.write(f"Average Tip Percentage: {average_tip:.2f}%\n")
    f.write(f"Best Tipping Day: {best_day}\n")


tips.groupby("day")["tip_percent"].mean().plot(kind="bar")
plt.title("Average Tip Percentage by Day")
plt.xlabel("Day")
plt.ylabel("Tip Percentage")
plt.tight_layout()
plt.savefig("avg_tip_by_day.png")
plt.show()

borough_avg_tip = tips.groupby("borough")["tip_percent"].mean()


best_borough = borough_avg_tip.idxmax()

print("Best Tipping Borough:", best_borough)


with open("results.txt", "a") as f:
    f.write("\nBorough Analysis:\n")
    f.write(borough_avg_tip.to_string())
    f.write(f"\nBest Tipping Borough: {best_borough}\n")


borough_avg_tip.sort_values().plot(kind="bar")
plt.title("Average Tip Percentage by Borough")
plt.xlabel("Borough")
plt.ylabel("Tip Percentage (%)")
plt.tight_layout()
plt.savefig("avg_tip_by_borough.png")
plt.show()