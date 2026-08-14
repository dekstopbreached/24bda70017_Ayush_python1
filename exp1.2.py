import matplotlib.pyplot as plt
import pandas as pd

# Create Dataset
week = list(range(1, 16))
hours_studied = [3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
marks = [42, 48, 50, 55, 58, 62, 65, 68, 70, 74, 78, 82, 85, 88, 90]
subjects = [f"Subject {i}" for i in range(1, 16)]

data = {
    "Week": week,
    "Hours_Studied": hours_studied,
    "Marks": marks,
    "Subject": subjects
}

df = pd.DataFrame(data)

plt.figure(figsize=(7,4))
plt.plot(df["Week"], df["Marks"],
         marker="o",
         linestyle="--",
         color="green")

plt.title("Student Marks Over Weeks")
plt.xlabel("Week")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

plt.figure(figsize=(7,4))
plt.scatter(df["Hours_Studied"],
            df["Marks"],
            color="purple",
            s=120)

plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()

plt.figure(figsize=(8,4))
plt.bar(df["Subject"],
        df["Marks"],
        color=["red","blue","green","orange","purple","brown"])

plt.title("Marks in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.xticks(rotation=15)
plt.show()