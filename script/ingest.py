import pandas as pd
import os


os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

data = {
    "student_id": [121, 122, 123,  124, 125],
    "name": ["Bisi", "Sade", "Michael", "Emmanuel", "Joseph"],
    "exam1": [95, 56, 72, 29, 84],
    "exam2": [65, 46, 70, 59, 88],
    "exam3": [49, 62, 85, 73, 92]
    
        }

df = pd.DataFrame(data)

raw_path = os.path.join("data", "raw", "student_exams.csv")
df.to_csv(raw_path, index=False)

print('Raw data successfully ingested in the raw folder')
print(df.head())