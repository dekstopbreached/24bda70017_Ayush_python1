
import pandas as pd

data = {
    'Employee_ID': ['E101', 'E102', 'E103', 'E104', 'E105', 'E106', 'E107'],
    'Name': ['Aarav', 'Reena Sharma', 'Kabir Singh', 'Ananya Mehta', 'Vivaan Kapoor', 'Meera Joshi', 'Arjun Reddy'],
    'UID': ['24bda7001', '24bda7002', '24bda7003', '24bda7004', '24bda7005', '24bda7006', '24bda7007'],
    'Salary': [35000, 42000, 38000, 45000, 39000, 42000, 47000],
    'Phone Number': ['9876543210', '8765432109', '7654321098', '6543210987', '5432109876', '4321098765', '3210987654'],
    'email': ['aarav@example.com', 'reena.sharma@example.com', 'kabir.singh@example.com', 'ananya.mehta@example.com', 'vivaan.kapoor@example.com', 'meera.joshi@example.com', 'arjun.reddy@example.com']
}

df = pd.DataFrame(data)
df.insert(0, 'S.No', range(1, len(df) + 1))

print("Employee Dataset:")
print(df)
print("-" * 30)

mean_salary = df['Salary'].mean()
median_salary = df['Salary'].median()
mode_salary = df['Salary'].mode()[0]
variance_salary = df['Salary'].var()
std_salary = df['Salary'].std()


print(f"Mean Salary: {mean_salary:.2f}")
print(f"Median Salary: {median_salary:.2f}")
print(f"Mode Salary: {mode_salary}")
print(f"Variance: {variance_salary:.2f}")
print(f"Standard Deviation: {std_salary:.2f}")

output_file = "employee_data.xlsx"
df.to_excel(output_file, index=False)
print(f"Excel file created: {output_file}")