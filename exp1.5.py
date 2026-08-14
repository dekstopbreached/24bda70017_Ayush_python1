import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
students = np.arange(1, 101)

data = {
    "Student_ID": students,
    "Attendance": np.random.randint(60, 101, 100),
    "Marks": np.random.randint(35, 101, 100),
    "Study_Hours": np.round(np.random.uniform(1, 8, 100), 1)
}

df = pd.DataFrame(data)

print("First 10 Students:")
print(df.head(10))

print("\nDescriptive Statistics:")
print(df[["Attendance", "Marks", "Study_Hours"]].describe())

print("\nMean:")
print(df[["Attendance", "Marks", "Study_Hours"]].mean())

print("\nMedian:")
print(df[["Attendance", "Marks", "Study_Hours"]].median())

print("\nMode:")
print(df[["Attendance", "Marks", "Study_Hours"]].mode().iloc[0])

print("\nVariance:")
print(df[["Attendance", "Marks", "Study_Hours"]].var())

print("\nStandard Deviation:")
print(df[["Attendance", "Marks", "Study_Hours"]].std())
# Mean
print("\nMean:")
print("Attendance :", df["Attendance"].mean())
print("Marks      :", df["Marks"].mean())
print("Study Hours:", df["Study_Hours"].mean())

# Median
print("\nMedian:")
print("Attendance :", df["Attendance"].median())
print("Marks      :", df["Marks"].median())
print("Study Hours:", df["Study_Hours"].median())

# Mode
print("\nMode:")
print("Attendance :", df["Attendance"].mode().tolist())
print("Marks      :", df["Marks"].mode().tolist())
print("Study Hours:", df["Study_Hours"].mode().tolist())

# Variance
print("\nVariance:")
print("Attendance :", df["Attendance"].var())
print("Marks      :", df["Marks"].var())
print("Study Hours:", df["Study_Hours"].var())

# Standard Deviation
print("\nStandard Deviation:")
print("Attendance :", df["Attendance"].std())
print("Marks      :", df["Marks"].std())
print("Study Hours:", df["Study_Hours"].std())

# Marks Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Marks"], bins=10, kde=True)
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()


# Attendance Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Attendance"], bins=10, kde=True)
plt.title("Distribution of Student Attendance")
plt.xlabel("Attendance (%)")
plt.ylabel("Number of Students")
plt.show()


# Box Plot of Marks
plt.figure(figsize=(6, 5))
sns.boxplot(y=df["Marks"])
plt.title("Box Plot of Student Marks")
plt.ylabel("Marks")
plt.show()

correlation = df["Study_Hours"].corr(df["Marks"])

print("\nCorrelation between Study Hours and Marks:")
print(correlation)

plt.figure(figsize=(8, 5))
sns.scatterplot(
    x=df["Study_Hours"],
    y=df["Marks"]
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

plt.figure(figsize=(7, 5))

sns.heatmap(
    df[["Attendance", "Marks", "Study_Hours"]].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

np.random.seed(42)

pass_simulation = np.random.binomial(
    n=100,
    p=0.70,
    size=10000
)

print("\nProbability Distribution:")
print(pd.Series(pass_simulation).describe())

plt.figure(figsize=(8, 5))

sns.histplot(
    pass_simulation,
    bins=20,
    kde=True
)

plt.title("Binomial Probability Distribution")
plt.xlabel("Number of Students Passing")
plt.ylabel("Frequency")
plt.show()

# Create 10 days of average marks
dates = pd.date_range(
    start="2026-08-01",
    periods=10
)

daily_marks = np.random.randint(60, 91, 10)

time_series = pd.DataFrame({
    "Date": dates,
    "Average_Marks": daily_marks
})

# Moving average
time_series["Moving_Average"] = (
    time_series["Average_Marks"]
    .rolling(window=3)
    .mean()
)

print("\nTime Series Data:")
print(time_series)


plt.figure(figsize=(9, 5))

plt.plot(
    time_series["Date"],
    time_series["Average_Marks"],
    marker="o",
    label="Average Marks"
)

plt.plot(
    time_series["Date"],
    time_series["Moving_Average"],
    marker="s",
    label="3-Day Moving Average"
)

plt.title("Time-Series Analysis of Average Marks")
plt.xlabel("Date")
plt.ylabel("Average Marks")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

df["Result"] = np.where(
    df["Marks"] >= 40,
    "Pass",
    "Fail"
)

print("\nPass/Fail Count:")
print(df["Result"].value_counts())


plt.figure(figsize=(6, 5))

sns.countplot(
    x=df["Result"]
)

plt.title("Pass vs Fail Students")
plt.xlabel("Result")
plt.ylabel("Number of Students")
plt.show()

print("\nFinal Dataset:")
print(df)

# Save data for Google Sheets / Excel
df.to_csv("100_students_analytics.csv", index=False)

print("\nDataset saved as 100_students_analytics.csv")