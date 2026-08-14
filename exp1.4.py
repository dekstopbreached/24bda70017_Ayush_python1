import pandas as pd
import matplotlib.pyplot as plt

# Weekly Weather Data
data = {
    "Date": [
        "30 Jul",
        "31 Jul",
        "1 Aug",
        "2 Aug",
        "3 Aug",
        "4 Aug",
        "5 Aug"
    ],
    "Morning (°C)": [27, 28, 29, 27, 26, 28, 29],
    "Afternoon (°C)": [33, 34, 35, 32, 31, 33, 36],
    "Evening (°C)": [30, 31, 32, 29, 28, 30, 32],
    "Night (°C)": [25, 26, 27, 24, 23, 25, 26]
}

# Create DataFrame
df = pd.DataFrame(data)

# Daily Average
df["Daily Average (°C)"] = df[
    ["Morning (°C)", "Afternoon (°C)", "Evening (°C)", "Night (°C)"]
].mean(axis=1).round(2)

# Weekly Averages
morning_avg = round(df["Morning (°C)"].mean(), 2)
afternoon_avg = round(df["Afternoon (°C)"].mean(), 2)
evening_avg = round(df["Evening (°C)"].mean(), 2)
night_avg = round(df["Night (°C)"].mean(), 2)
weekly_avg = round(df["Daily Average (°C)"].mean(), 2)

# Weekly Summary Table
summary = pd.DataFrame({
    "Category": [
        "Morning Average",
        "Afternoon Average",
        "Evening Average",
        "Night Average",
        "Overall Weekly Average"
    ],
    "Temperature (°C)": [
        morning_avg,
        afternoon_avg,
        evening_avg,
        night_avg,
        weekly_avg
    ]
})

# Save to Excel
with pd.ExcelWriter("Weekly_Weather_Report.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Weather Data", index=False)
    summary.to_excel(writer, sheet_name="Weekly Summary", index=False)

print("Excel file created successfully!")

print("\nWeather Data")
print(df)

print("\nWeekly Summary")
print(summary)

# -------------------- Line Chart --------------------

plt.figure(figsize=(10,6))

plt.plot(df["Date"], df["Morning (°C)"],
         marker='o', linewidth=2, label="Morning")

plt.plot(df["Date"], df["Afternoon (°C)"],
         marker='s', linewidth=2, label="Afternoon")

plt.plot(df["Date"], df["Evening (°C)"],
         marker='^', linewidth=2, label="Evening")

plt.plot(df["Date"], df["Night (°C)"],
         marker='d', linewidth=2, label="Night")

plt.plot(df["Date"], df["Daily Average (°C)"],
         marker='*', linewidth=3, linestyle='--',
         label="Daily Average")

plt.title("Weekly Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()