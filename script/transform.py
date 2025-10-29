import pandas as pd
import os


raw_path= os.path.join("data", "raw", "student_exams.csv")
processed_path= os.path.join("data", "processed", "student_exam_cleaned.csv")


df = pd.read_csv(raw_path)

df.to_csv(processed_path, index=False)
print("Cleaned data saved to", processed_path)


df['total_score'] = (df['exam1'] + df['exam2']) + df['exam3']

df['avg_score']  = (df['total_score']/ 3)


# Define grading function
def grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'
    
df['grade_per_student'] = df['avg_score'].apply(grade)

# Determine pass/fail
df["status"] = df["grade_per_student"].apply(lambda x: "Passed" if x != "F" else "Failed")
print(df.head())

# Count how many students passed
passed_count = len(df[df["grade_per_student"] != "F"])
print(f"Number of students who passed: {passed_count}")