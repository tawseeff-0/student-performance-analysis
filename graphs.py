import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("student_results.csv")

# Subjects
subjects = ["Math", "Science", "English", "Computer"]

# Create Grade Column if Missing
def calculate_grade(p):
    if p >= 90:
        return "A"
    elif p >= 80:
        return "B"
    elif p >= 70:
        return "C"
    elif p >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Percentage"].apply(calculate_grade)

# Save Updated Dataset
df.to_csv("student_results.csv", index=False)

sns.set_theme(style="whitegrid")

# GRAPH 1: BAR PLOT
plt.figure(figsize=(9, 5))
df[subjects].mean().plot(kind="bar")
plt.title("Subject Wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("graph1.png")
plt.show()
plt.close()

# GRAPH 2: PIE CHART
plt.figure(figsize=(7, 7))
df["Grade"].value_counts().plot(
    kind="pie", autopct="%1.1f%%"
)
plt.title("Student Grade Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("graph2.png")
plt.show()
plt.close()

# GRAPH 3: HISTOGRAM
plt.figure(figsize=(9, 5))
plt.hist(df["Percentage"], bins=5, edgecolor="black")
plt.title("Student Percentage Distribution")
plt.xlabel("Percentage")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("graph3.png")
plt.show()
plt.close()

# GRAPH 4: SCATTER PLOT
plt.figure(figsize=(9, 5))
sns.scatterplot(
    data=df,
    x="Attendance",
    y="Percentage",
    hue="Grade",
    s=100
)
plt.title("Attendance vs Student Performance")
plt.tight_layout()
plt.savefig("graph4.png")
plt.show()
plt.close()

# GRAPH 5: HEATMAP
plt.figure(figsize=(9, 6))
sns.heatmap(
    df[subjects].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Subject Marks Correlation")
plt.tight_layout()
plt.savefig("graph5.png")
plt.show()
plt.close()

print("\n================================")
print("ALL 5 GRAPHS GENERATED SUCCESSFULLY!")
print("================================")
