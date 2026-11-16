import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("students.csv")

# Display Dataset
print("\n===== STUDENT PERFORMANCE ANALYSIS =====")
print(df)

# Calculate Total Marks
subjects = ["Math", "Science", "English", "Computer"]

df["Total_Marks"] = df[subjects].sum(axis=1)

# Calculate Percentage
df["Percentage"] = (df["Total_Marks"] / 400) * 100

# Calculate Average
average_marks = np.mean(df["Percentage"])

# Top Performer
top_student = df.loc[df["Percentage"].idxmax()]

print("\n===== ANALYSIS RESULTS =====")
print("Average Percentage:", round(average_marks, 2))

print("\n===== TOP PERFORMER =====")
print(top_student)

# Subject Wise Average
print("\n===== SUBJECT AVERAGE =====")
print(df[subjects].mean())

# Save Results
df.to_csv("student_results.csv", index=False)

print("\nResults saved successfully!")